from core.BaseBot import BaseBot
import traceback


class TenRecitations(BaseBot):
    def clean_text(self, text):
        text = text.replace('\n', '').replace('\t', '').replace('  ', ' ')
        text = text.replace('\xa0', '').strip()
        return text

    def parse_difference(self, text):
        differences = {}
        portion_of_ayah = self.clean_text(text.find('strong').text)
        difference_in_ayah = text.find('h2').text
        difference_in_ayah = self.clean_text(difference_in_ayah[:difference_in_ayah.find('\n')])
        difference_in_recitations = text.find('h2').find_all('div', class_='quran-page')
        for difference_in_recitation in difference_in_recitations:
            reciter_name = self.clean_text(difference_in_recitation.find('ol').text.replace('\n', ','))
            recitation = self.clean_text(difference_in_recitation.find('li').text)
            differences[reciter_name] = recitation
        return {
            'portion_of_ayah': portion_of_ayah,
            'difference_in_ayah': difference_in_ayah,
            'difference_in_recitations': differences
        }


    def get_ayah(self, surah_no, ayah_no):
        url = f'https://www.nquran.com/ar/index.php?group=tb1&tpath=2&aya_no={ayah_no}&sorano={surah_no}&mRwai='
        page = self.html.get_page(url=url)

        # differences = response_html.find(id='detail').find('div', class_='blockrwaya').find_all(recursive=False)
        detail = self.html.find_by_id(page, 'detail')
        blockrwaya = self.html.find_by_class(detail, 'blockrwaya')
        differences = self.html.find_all(blockrwaya, recursive=False)

        differences_result = [self.parse_difference(difference) for difference in differences]
        return differences_result

    async def start(update, context):
        await update.message.reply_text("Bot has started")

    async def text(self, update, context):
        try:
            message = update.message.text
            surah_no, ayah_no = message.split()
            sections = self.get_ayah(surah_no, ayah_no)
            for section in sections:
                message_text = f"*الآية:* _{section['portion_of_ayah']}_\n"
                message_text += f"*الموضع:* _{section['difference_in_ayah']}_\n\n"
                message_text += "*الفروقات:*\n"
                for key, value in section['difference_in_recitations'].items():
                    message_text += f"\n- *{key}* \n{value}\n"
                await update.message.reply_text(message_text, parse_mode='Markdown')
        except:
            print(traceback.format_exc())
            await update.message.reply_text("هذه الآية ليس فيها خلاف، أو أن السورة لا تحتوي على الآية التي طلبتها.")
