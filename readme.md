### running the tailwind 
1. download the standalone tailwind executable from [here](https://tailwindcss.com/blog/standalone-cli)
2. run `tailwindcss-windows-x64.exe -i .\static\input.css -o .\static\output.css --watch`
3. if on macos run `./tailwindcss-macos-x64 -i ./static/input.css -o ./static/output.css --watch`

### this actually runs pretty well. You can try it on your own machine if you want.

1. clone the repo with `git clone ...`
2. pull the large files with `git lfs pull`
3. run `pip install -r requirements.txt`
4. run `python manage.py runserver`
5. go to `http://127.0.0.1:8000/` in your browser

isn't hosted yet for all to see, but will be soon enough.

### vision
1. review profs, courses, and programs
2. compare courses across schools for exchanges, selecting programs
3. track and plan your progress throughout school
4. get resources for the classes, as recommended by people who've done it before.

### todo!

#### main pages
1. course page [title, ratings, add review, list reviews]
2. make course table nice [code, title, ratings]
2. filtering courses [level, rating, department, program]
3. school page [tab between courses, departments, profs, programs]
4. prof page [title, ratings, add review, list reviews]
5. program page [title, ratings, add review, list reviews]
6. user page [profile, reviews, courses, program]

### Scraping the data
scraping data across universities - ask the cs clubs nicely
scraping good quality data across universities - use ai on crawled pages

1. course code, description, faculty, credits, pre/co/anti reqs, link to offical site
2. faculty: name, maybe description, site, needed just to filter courses
3. profs: name, page for more info, picture
4. programs: required courses, pages for more detail

### gimmicky features for fun
1. productivity app (pomodoro, time tracker, etc) (but competitive, since people will see how long they spent)
2. flashcards and resources for the classes
3. blogposting / about page
4. ai summaries / review improvers (suggest things)
5. cool stats on the courses, like how many people took it, how many people liked it, etc
6. steam like reviews (funny reviews, helpful reviews, etc)
7. course recommendations (based on what you've taken, what you like, etc)
8. steam like ratings (mostly positive, mostly negative etc. , etc)