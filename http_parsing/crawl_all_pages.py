import urllib.request as urlrq
from collections import Counter
from collections import defaultdict
from urllib.parse import urlparse

import certifi
from bs4 import BeautifulSoup
from bs4.element import Comment

stopwords = set(
    ['ourselves', 'hers', 'between', 'yourself', 'but', 'again', 'there', 'about', 'once', 'during', 'out', 'very',
     'having', 'with', 'they', 'own', 'an', 'be', 'some', ' for ', 'do', 'its', 'yours', 'such', 'into', 'of',
     'most',
     'itself', 'other', 'off', ' is ', 's', 'am', ' or ', 'who', 'as', 'from ', 'him', 'each', 'the', 'themselves',
     'until', 'below', 'are', 'we', 'these', 'your', 'his', 'through', 'don', 'nor', 'me', 'were', 'her', 'more',
     'himself', 'this', 'down', 'should', 'our', 'their', 'while ', 'above', 'both', 'up', 'to', 'ours', 'had',
     'she',
     'all', 'no', 'when', 'at', 'any', 'before', 'them', 'same', ' and ', 'been', 'have', ' in ', 'will', 'on',
     'does',
     'yourselves', 'then', 'that', 'because', 'what', 'over', 'why', 'so', 'can', 'did', ' not ', 'now', 'under',
     'he',
     'you', 'herself', 'has', 'just', 'where', 'too', 'only', 'myself', 'which', 'those', 'i', 'after', 'few',
     'whom',
     't', 'being', ' if ', 'theirs', 'my', 'against', 'a', 'by', 'doing', 'it', 'how', 'further', 'was', 'here',
     'than', '&', '-', 'and', 'from', 'is', 'for', '=', ',', 'the', 'in'])


def crawl_urls(url_list, crawled_urls, url, domain):
    """ get a set of urls and crawl each url recursively"""
    print("parsing {}".format(url))
    # Once the url is parsed, add it to crawled url list
    crawled_urls.append(url)
    html = urlrq.urlopen(url, cafile=certifi.where()).read()
    soup = BeautifulSoup(html, features="lxml")
    urls = soup.findAll("a")

    # Even if the url is not part of the same domain, it is still collected
    # But those urls not in the same domain are not parsed
    for a in urls:
        if (a.get("href")) and (a.get("href") not in url_list):
            url_list.append(a.get("href"))

    # Recursively parse each url within same domain
    for page in set(url_list):  # set to remove duplicates
        # Check if the url belong to the same domain And if this url is already parsed ignore it
        if (urlparse(page).netloc == domain) and (page not in crawled_urls):
            crawl_urls(url_list, crawled_urls, page, domain)

    # Once all urls are crawled return the list to calling function
    else:
        return crawled_urls, url_list


def fetch_valid_urls(urls, parent_url):
    result = []
    for url in urls:
        if url[0] == '/':
            result.append(parent_url + url)

    print(result)
    return result


def tag_visible(element):
    if element.parent.name in ['style', 'script', 'head', 'title', 'meta', '[document]']:
        return False
    if isinstance(element, Comment):
        return False
    return True


def get_top_10_words(list_words):
    wordcount = {}
    # To eliminate duplicates, remember to split by punctuation, and use case demiliters.
    for words in list_words:
        for word in words.split(' '):
            if word.lower() not in stopwords:
                if word not in wordcount:
                    wordcount[word] = 1
                else:
                    wordcount[word] += 1
    if '' in wordcount:
        del wordcount['']

    word_counter = Counter(wordcount)
    top_10 = word_counter.most_common(10)
    print(top_10)
    return top_10


def extract_words(valid_urls):
    urls_dict = defaultdict(lambda: ('title', list))
    for i, link in enumerate(valid_urls):
        html = urlrq.urlopen(link, cafile=certifi.where()).read()
        soup = BeautifulSoup(html, features="lxml")
        title = soup.title.string
        print(title)
        texts = soup.findAll(text=True)
        visible_texts = filter(tag_visible, texts)
        list_words = [t.strip() for t in visible_texts if t.strip() is not ""]
        top_10_words = get_top_10_words(list_words)
        urls_dict[link] = (title, top_10_words)
        # if i == 2:
        #     break
    return urls_dict
    # print(urls_dict)


def crawl_page(parent_url, unique_id):
    url_list = list()
    crawled_urls = list()
    url_list.append(parent_url)
    domain = urlparse(parent_url).netloc
    crawled_urls, url_list = crawl_urls(url_list, crawled_urls, parent_url, domain)
    print(crawled_urls)
    print(url_list)
    valid_urls = fetch_valid_urls(url_list, parent_url)
    # store these results against unique_id in db
    return extract_words(valid_urls)


if __name__ == "__main__":
    parent_url = "https://www.greatlearning.in/"
    url_list = list()
    crawled_urls = list()
    url_list.append(parent_url)
    domain = urlparse(parent_url).netloc
    crawled_urls, url_list = crawl_urls(url_list, crawled_urls, parent_url, domain)
    print(crawled_urls)
    print(url_list)
    valid_urls = fetch_valid_urls(url_list, parent_url)
    # store these results against unique_id in db
    print(extract_words(valid_urls))

# defaultdict(<function extract_words.<locals>.<lambda> at 0x10ef06e18>, {'https://www.greatlearning.in//': ('Great Learning: Top-Ranked Professional Courses for Career Success', [('Business', 28), ('PGP', 26), ('12', 25), ('2019', 22), ('Analytics', 20), ('Learning', 20), ('Online', 19), ('|', 18), ('today', 18), ('Certificate', 17)]), 'https://www.greatlearning.in//pg-program-business-analytics-course': ('Business analytics course, [Get Average Salary Hike upto 50%]- Great Learning', [('Business', 89), ('Analytics', 71), ('Data', 44), ('Great', 42), ('data', 32), ('Learning', 26), ('business', 24), ('using', 23), ('online', 23), ('analytics', 22)]), 'https://www.greatlearning.in//pg-program-data-science-course': ('Data Science Course, [Get 65% Average Salary Hike]- Great Learning', [('Data', 64), ('data', 54), ('science', 33), ('Science', 32), ('Great', 29), ('candidates', 24), ('Learning', 23), ('Analytics', 22), ('Business', 21), ('online', 21)]), 'https://www.greatlearning.in//7-months-program-business-analytics': ('Business analyst certification, Business analyst course, Business analyst training  | Great Learning', [('Analytics', 34), ('Great', 29), ('Program', 27), ('Business', 26), ('using', 22), ('Learning', 22), ('learning', 21), ('Data', 20), ('Know', 20), ('Lakes', 17)]), 'https://www.greatlearning.in//pg-program-dsba': ('Data Science, Business Analytics Course [Learn from UT Austin Faculty]-Great Learning', [('Business', 57), ('Analytics', 56), ('Data', 43), ('Science', 41), ('Great', 35), ('Learning', 23), ('using', 22), ('Lakes', 20), ('Know', 20), ('Program', 19)]), 'https://www.greatlearning.in//business-analytics-certificate-course': ('Business Analyst Certification, Analytics Course [Learn from the Best]-Great Learning', [('Analytics', 56), ('Business', 55), ('analytics', 40), ('business', 37), ('Data', 33), ('Certificate', 33), ('industry', 27), ('Great', 23), ('learning', 21), ('Learning', 20)]), 'https://www.greatlearning.in//courses/analytics-using-excel': ('Data Analytics using Excel with Great Learning', [('Data', 23), ('PGP', 16), ('using', 14), ('data', 14), ('Business', 13), ('Analytics', 13), ('Excel', 13), ('Program', 11), ('Learning', 11), ('Course', 9)]), 'https://www.greatlearning.in//pg-program-artificial-intelligence-course': ('Artificial Intelligence Course, [Learn from The University of Texas, Austin Faculty]- Great Learning', [('Intelligence', 72), ('Artificial', 68), ('Learning', 62), ('Machine', 33), ('Great', 33), ('AI', 26), ('course', 25), ('or', 20), ('learn', 19), ('online', 19)]), 'https://www.greatlearning.in//pg-program-machine-learning-course': ('Machine Learning Course, [Learn from India’s Top 10 Ranked Faculty]- Great Learning', [('learning', 68), ('Learning', 67), ('Machine', 66), ('machine', 49), ('online', 28), ('Data', 26), ('Great', 22), ('data', 19), ('PGP', 17), ('course', 17)]), 'https://www.greatlearning.in//artificial-intelligence-course-for-managers-leaders': ('AI Course for Business Leaders & Professionals [Coding Experience not necessary]', [('Learning', 21), ('AI', 19), ('Business', 18), ('PGP', 18), ('Program', 18), ('Intelligence', 17), ('Artificial', 13), ('Machine', 11), ('learning', 11), ('Analytics', 10)]), 'https://www.greatlearning.in//deep-learning-course': ('Deep Learning Certificate Program and Online Training courses in India | Great Learning', [('learning', 67), ('Learning', 61), ('Deep', 38), ('deep', 37), ('Great', 24), ('Program', 19), ('Machine', 19), ('PGP', 18), ('projects', 17), ('sessions', 16)]), 'https://www.greatlearning.in//pg-program-cloud-computing-course': ('Cloud Computing Course, [Get AWS Educate Cloud Badge]- Great Learning', [('cloud', 73), ('Cloud', 61), ('AWS', 43), ('computing', 34), ('course', 28), ('Learning', 27), ('Great', 27), ('learning', 21), ('Computing', 20), ('done', 20)]), 'https://www.greatlearning.in//devops-certification-course': ('Devops Certification Course, [Learn from the Best]- Great Learning', [('DevOps', 64), ('PGP', 16), ('Learning', 16), ('Great', 16), ('course', 15), ('Engineer', 14), ('AWS', 14), ('Business', 13), ('Program', 13), ('development', 13)]), 'https://www.greatlearning.in//online-cyber-security-course': ('Cyber Security Course, [Learn from Stanford Faculty]- Great Learning', [('security', 62), ('Security', 57), ('cyber', 45), ('Stanford', 38), ('Cyber', 35), ('Program', 24), ('course', 21), ('Great', 18), ('Learning', 17), ('PGP', 16)]), 'https://www.greatlearning.in//full-stack-developer-course': ('Full Stack Developer Course, [Get Average Starting Salary 9LPA]- Great Learning', [('stack', 35), ('full', 34), ('Learning', 27), ('Full', 26), ('development', 25), ('course', 24), ('Stack', 21), ('Great', 19), ('PGP', 16), ('developer', 16)]), 'https://www.greatlearning.in//design-thinking-course': ('Design Thinking Course, [Learn Design Thinking from Stanford GSB]-Great Learning', [('thinking', 48), ('Design', 44), ('design', 44), ('Business', 29), ('Thinking', 25), ('course', 24), ('Stanford', 19), ('School', 17), ('PGP', 16), ('helps', 16)]), 'https://www.greatlearning.in//digital-business-course': ('PG Diploma in Digital Business, Digital Business Course [Learn from Purdue]-Great Learning', [('Digital', 27), ('Business', 25), ('Learning', 17), ('PGP', 16), ('Analytics', 15), ('Program', 13), ('Data', 9), ('Purdue', 9), ('University', 9), ('Intelligence', 8)]), 'https://www.greatlearning.in//pg-program-strategic-digital-marketing-course': ('Strategic Digital Marketing Course, [Learn from the Best]- Great Learning', [('Marketing', 52), ('marketing', 49), ('Digital', 44), ('digital', 38), ('Great', 28), ('Learning', 22), ('online', 18), ('course', 18), ('PGP', 16), ('Business', 15)]), 'https://www.greatlearning.in//gl-excelerate': ('GL Excelerate | Get the career leap you deserve', [('PGP', 16), ('Business', 13), ('Career', 11), ('Get', 11), ('Analytics', 10), ('Program', 10), ('Learning', 9), ('Intelligence', 7), ('Data', 6), ('Certificate', 6)]), 'https://www.greatlearning.in//gl-excelerate#career': ('GL Excelerate | Get the career leap you deserve', [('PGP', 16), ('Business', 13), ('Career', 11), ('Get', 11), ('Analytics', 10), ('Program', 10), ('Learning', 9), ('Intelligence', 7), ('Data', 6), ('Certificate', 6)]), 'https://www.greatlearning.in//gl-excelerate#jobBoard': ('GL Excelerate | Get the career leap you deserve', [('PGP', 16), ('Business', 13), ('Career', 11), ('Get', 11), ('Analytics', 10), ('Program', 10), ('Learning', 9), ('Intelligence', 7), ('Data', 6), ('Certificate', 6)]), 'https://www.greatlearning.in//gl-excelerate#hackathons': ('GL Excelerate | Get the career leap you deserve', [('PGP', 16), ('Business', 13), ('Career', 11), ('Get', 11), ('Analytics', 10), ('Program', 10), ('Learning', 9), ('Intelligence', 7), ('Data', 6), ('Certificate', 6)]), 'https://www.greatlearning.in//gl-excelerate#liveProject': ('GL Excelerate | Get the career leap you deserve', [('PGP', 16), ('Business', 13), ('Career', 11), ('Get', 11), ('Analytics', 10), ('Program', 10), ('Learning', 9), ('Intelligence', 7), ('Data', 6), ('Certificate', 6)]), 'https://www.greatlearning.in//gl-excelerate#careerMentorship': ('GL Excelerate | Get the career leap you deserve', [('PGP', 16), ('Business', 13), ('Career', 11), ('Get', 11), ('Analytics', 10), ('Program', 10), ('Learning', 9), ('Intelligence', 7), ('Data', 6), ('Certificate', 6)]), 'https://www.greatlearning.in//alumni': ('Alumni | Great Learning', [('Read', 36), ('full', 35), ('story', 35), ('arrow_right_alt', 35), ('Analytics', 21), ('Data', 18), ('Business', 17), ('PGP', 16), ('Program', 13), ('Learning', 13)]), 'https://www.greatlearning.in//gl-academy': ('Great Learning Academy', [('PGP', 8), ('Learning', 8), ('Business', 7), ('Analytics', 6), ('Great', 6), ('Program', 5), ('Data', 4), ('Intelligence', 4), ('Career', 4), ('For\n', 4)]), 'https://www.greatlearning.in//hire-talent': ('Hire Job-Ready Tech Professionals', [('Business', 22), ('PGP', 16), ('Analyst', 14), ('Analytics', 13), ('Learning', 12), ('Program', 11), ('Data', 10), ('Intelligence', 8), ('Machine', 7), ('Hire', 7)]), 'https://www.greatlearning.in//about-us': ('About Great Learning', [('Read', 52), ('2018', 34), ('2019', 20), ('Business', 19), ('Learning', 17), ('PGP', 16), ('Program', 15), ('Analytics', 14), ('Created', 10), ('Sketch.', 10)]), 'https://www.greatlearning.in//blog/': ('Blog- A platform to showcase all the learnings and experiences of Big Data and Analytics', [('Data', 22), ('Analytics', 21), ('Business', 18), ('Science', 17), ('PGP', 16), ('Learning', 14), ('Machine', 10), ('Program', 10), ('2019', 10), ('Read', 10)]), 'https://www.greatlearning.in//about-us#more_media': ('About Great Learning', [('Read', 52), ('2018', 34), ('2019', 20), ('Business', 19), ('Learning', 17), ('PGP', 16), ('Program', 15), ('Analytics', 14), ('Created', 10), ('Sketch.', 10)]), 'https://www.greatlearning.in//careers': ('Careers with Great Learning', [('Send', 32), ('careers@greatlearning.in', 32), ('READ', 32), ('like', 29), ('Manager', 27), ('job', 27), ('learning', 27), ('work', 25), ('Bangalore,', 25), ('Learning', 23)]), 'https://www.greatlearning.in//contactus': ('Contact Great Learning', [('PGP', 16), ('Business', 14), ('Analytics', 10), ('Program', 10), ('Learning', 9), ('Created', 8), ('Sketch.', 8), ('Intelligence', 7), ('Data', 6), ('Certificate', 6)]), 'https://www.greatlearning.in//privacy-policy': ('Privacy Policy | Great Learning', [('or', 131), ('data', 112), ('use', 60), ('may', 57), ('Data', 41), ('us', 34), ('Great', 33), ('Services', 31), ('cookies', 30), ('Learning', 28)]), 'https://www.greatlearning.in//terms': ('greatlearning', [('or', 86), ('Great', 30), ('Learning', 28), ('not', 27), ('may', 22), ('use', 22), ('OR', 22), ('Services', 21), ('PGP', 16), ('Terms', 16)]), 'https://www.greatlearning.in//events/upcoming': ('Events @ Great Learning | Stay Abreast on Advanced analytics, big data and business intelligence technologies', [('PGP', 14), ('Business', 12), ('Program', 10), ('Analytics', 10), ('Learning', 8), ('Certificate', 6), ('Data', 6), ('Years', 6), ('Intelligence', 5), ('Machine', 5)]), 'https://www.greatlearning.in//gl4l': ('\n      Great Learning - Get started with Data Science | GL4L\n    ', [('Business', 18), ('PGP', 17), ('Learning', 16), ('Data', 16), ('Analytics', 14), ('Program', 14), ('Start', 12), ('Machine', 9), ('Science', 9), ('Certificate', 8)])})
