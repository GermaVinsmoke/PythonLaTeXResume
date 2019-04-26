import requests
import bs4 as bs
from urllib.parse import quote_plus


def update_resume():
    repurl = 'https://api.stackexchange.com/2.2/users/8437974?order=desc&sort=reputation&site=stackoverflow'
    result = requests.get(repurl)
    reputation = result.json()['items'][0]['reputation']

    url = 'https://stackoverflow.com/users/story/8437974'
    page = requests.get(url)
    soup = bs.BeautifulSoup(page.text, 'lxml')

    temp_soup = soup.find('div', {'class': 'tag-wrapper'})
    numbers = temp_soup.find_all('div', {'class': 'number'})
    tags = temp_soup.find_all('span', {'class': 'post-tag'})
    data = {}
    for i, j in zip(numbers, tags):
        data[i.next_element] = j.text
    keys = list(data.keys())

    profile_temp_soup = soup.find('div', {'id': 'user-card'})
    print(profile_temp_soup)

    tex = r'''
    \documentclass[letterpaper, 11pt]{article}

    \usepackage{latexsym}
    \usepackage[empty]{fullpage}
    \usepackage{titlesec}
    \usepackage{marvosym}
    \usepackage{bookmark}
    \usepackage[usenames,dvipsnames]{color}
    \usepackage{verbatim}
    \usepackage{enumitem}
    \usepackage{fancyhdr}
    
    \pagestyle{fancy}
        \fancyhf{}
        \fancyfoot{}
        \renewcommand{\headrulewidth}{0pt}
        \renewcommand{\footrulewidth}{0pt}
      
      
        \addtolength{\oddsidemargin}{-0.375in}
        \addtolength{\evensidemargin}{-0.375in}
        \addtolength{\textwidth}{1in}
        \addtolength{\topmargin}{-.5in}
        \addtolength{\textheight}{1.0in}
      
        \urlstyle{same}
      
        \raggedbottom
        \raggedright
        \setlength{\tabcolsep}{0in}
      
      
        \titleformat{\section}{
          \vspace{-4pt}\scshape\raggedright\large
        }{}{0em}{}[\color{black}\titlerule \vspace{-5pt}]
      
      
        \newcommand{\resumeItem}[2]{
          \item\small{
            \textbf{#1}{: #2 \vspace{-2pt}}
          }
        }
      
        \newcommand{\resumeSubheading}[4]{
          \vspace{-1pt}\item
            \begin{tabular*}{0.97\textwidth}{l@{\extracolsep{\fill}}r}
              \textbf{#1} & #2 \\
              \textit{\small#3} & \textit{\small #4} \\
            \end{tabular*}\vspace{-5pt}
        }
      
        \newcommand{\resumeSubItem}[2]{\resumeItem{#1}{#2}\vspace{-4pt}}
      
        \renewcommand{\labelitemii}{$\circ$}
      
        \newcommand{\resumeSubHeadingListStart}{\begin{itemize}[leftmargin=*]}
        \newcommand{\resumeSubHeadingListEnd}{\end{itemize}}
        \newcommand{\resumeItemListStart}{\begin{itemize}}
        \newcommand{\resumeItemListEnd}{\end{itemize}\vspace{-5pt}}
      
      
        \definecolor{lightGray}{gray}{0.6}
        \definecolor{darkGray}{gray}{0.3}
    
    \begin{document}
    
    \begin{tabular*}{\textwidth}{l@{\extracolsep{\fill}}r}
          \textbf{}{\Large Vaibhav Dangra} & E-mail - \href{mailto:vaibhav1180@gmail.com}{vaibhav1180@gmail.com} \\
            \today & Phone - +91-87-5069-3452 \\
        \end{tabular*}
    
    \section{Objective}
            {Seeking employment in a fast growing organization so as to hone my tecnical skills and attaining excellent standards while meeting organizational needs.}
    
    \section{Education}
          \resumeSubHeadingListStart
        \resumeSubheading
          {The Northcap University}
          {\color{lightGray}Gurugram, India}
          {Bachelor of Technology, Computer Science, CGPA: 8.41}
          {\color{lightGray}2016-2020}
            \resumeSubheading
              {Greenwood Public School}
              {\color{lightGray}Gurugram, India}
              {All India Senior School Certificate Examination, CBSE, Percentage: 89.2}
              {\color{lightGray}May 2016}
            \resumeSubheading
              {Greenwood Public School}
              {\color{lightGray}Gurugram, India}
              {All India Secondary School Examination, CBSE;  CGPA: 10/10}
              {\color{lightGray}May 2014}
              \vspace{-3.5mm}
          \resumeSubHeadingListEnd
    
    \section{Work Experience}
          \resumeSubHeadingListStart
            \resumeSubheading
              {Mobile App Development}
          {\color{lightGray}Pizza Hut, Gamma Pizzakraft Pvt. Ltd.}
          {UI/UX Developer}
          {\color{lightGray}May 2018 - September 2018}
          \resumeItemListStart
           \item{Unity based Android application for some lucky customers}
           \vspace{-1.5mm}
          \resumeItemListEnd
          {\color{darkGray}Technologies: Unity, Unity Script, Blender, Adobe Photoshop, Git}
        \resumeSubheading
              {Software Development}
          {\color{lightGray}Padhle.com (Online Edu. Portal)}
          {Web Scraping}
          {\color{lightGray}July 2018 - August 2018}
          \resumeItemListStart
           \item{Web scraping in order to download PDF files}
           \vspace{-1.5mm}
          \resumeItemListEnd
          {\color{darkGray}Technologies: Python, Selenium, BeautifulSoup, Requests, Git}
          \resumeSubHeadingListEnd
    
    \section{Projects}
        \resumeSubHeadingListStart
          \resumeSubheading
            {Phrase Generator}
            {\color{lightGray}Personal project}
            {Genetic Algorithm}
            {\color{lightGray}April 2018 - June 2018}
            \resumeItemListStart
             \item{Generates a desired phrase with the help of {\textbf {Selection}}, {\textbf {Crossover}} and {\textbf{Mutation}}}
             \vspace{-1.5mm}
            \resumeItemListEnd
            {\color{darkGray}Technologies: Java}
          \resumeSubheading
            {Movie Rating Analysis}
            {\color{lightGray}Personal project}
            {Web Scraping and IMDb API}
            {\color{lightGray}Oct 2018 - Present}
            \resumeItemListStart
             \item{CLI based app for comparing movie ratings}
             \vspace{-1.5mm}
            \resumeItemListEnd
            {\color{darkGray}Technologies: Python, IMDb API, Requests, BeautifulSoup, Matplotlib}
          \resumeSubheading
            {Virtual Classroom}
            {\color{lightGray}BTech Major project}
            {Website Development}
            {\color{lightGray}Jan 2019 - Present}
            \resumeItemListStart
             \item{Live streaming web based app in order to enhance the learning of students with features like live lectures, discussion forms and content sharing}
             \vspace{-1.5mm}
            \resumeItemListEnd
            {\color{darkGray}Technologies: ReactJS, Redux, MaterializeCSS, CSS, Git, Firebase(Database, Auth.)}
          \resumeSubheading
            {Reactize}
            {\color{lightGray}Personal project}
            {FrontEnd Development}
            {\color{lightGray}March 2019}
            \resumeItemListStart
             \item{Implementation of MaterializeCSS JS components in ReactJS}
             \vspace{-1.5mm}
             \resumeItemListEnd
             {\color{darkGray} Technologies: ReactJS, Redux, MaterializeCSS, HTML, CSS, Heroku, Git}
        \resumeSubHeadingListEnd
    
    \section{Strengths}
        \resumeItemListStart
         \item{Ability to work together in a team and individually}
         \item{Ability to perform multiple tasks}
         \item{Quick Learner}	
        \resumeItemListEnd
    
    \section{Hobbies}
        \resumeItemListStart
         \item{Watching anime}
         \item{Drawing anime characters}
         \item{Q and A on Stack Overflow(Reputation: %(rep)s, Top %(keys[0])s percent in %(data['5'])s, Top %(keys[1])s percent in %(data['20'])s)}
        \resumeItemListEnd
    \end{document}
    ''' % {'rep': reputation, 'keys[0]':  format(keys[0]), "data['5']": format(data['5']), 'keys[1]': format(keys[1]), "data['20']": format(data['20'])}
          # (keys[0], data['5'], keys[1], data['20'])

    # print(tex)
    ltx = requests.get(f'https://latexonline.cc/compile?text={quote_plus(tex)}&force=true')
    # print('Status code: ',ltx.status_code)
    with open('vaibhav_resume.pdf', 'wb') as f:
        print(ltx.content)
        f.write(ltx.content)


if __name__ == "__main__":
    update_resume()
