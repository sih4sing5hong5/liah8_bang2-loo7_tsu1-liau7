# Scrapy settings for liah8_TGB project
#
# For simplicity, this file contains only the most important settings by
# default. All the other settings are documented here:
#
#     http://doc.scrapy.org/en/latest/topics/settings.html
#

BOT_NAME = 'liah8_bang7_loo7_tsu1_liau7'

SPIDER_MODULES = ['liah8_bang7_loo7_tsu1_liau7.spiders']
NEWSPIDER_MODULE = 'liah8_bang7_loo7_tsu1_liau7.spiders'

ITEM_PIPELINES = {
    'liah8_bang7_loo7_tsu1_liau7.pipelines.Bang7Loo7Pipeline': 300,
}
# Crawl responsibly by identifying yourself (and your website) on the user-agent
# USER_AGENT = 'liah8_TGB (+http://www.yourdomain.com)'
DOWNLOAD_DELAY = 0.05
RANDOMIZE_DOWNLOAD_DELAY = True
CONCURRENT_REQUESTS_PER_IP = 2
