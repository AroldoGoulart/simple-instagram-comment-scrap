# Instagram Comments Scraper

## Installation
1. Clone the repository:
   - `git clone git@github.com:AroldoGoulart/simple-instagram-comment-scrap.git`
   or 
   - `git clone https://github.com/AroldoGoulart/simple-instagram-comment-scrap.git`
   or download the [zip](https://github.com/AroldoGoulart/simple-instagram-comment-scrap/archive/master.zip)

2. Create a Virtual Environment (Recommended):
   - `pip install virtualenv`
   - `virtualenv .venv`

3. Activate the virtual environment:
   - For Unix/Mac: `source .venv/bin/activate`
   - For Windows: `.venv\Scripts\activate`

4. Install dependencies:
   - `pip install -r requirements.txt`

5. Login:
   - Replace `'USER-NAME'` with your username in `username.send_keys ('USER-NAME')`
   - Replace `'PASSWORD'` with your password in `password.send_keys('PASSWORD')`
   - Note: We don't store your password.

6. Run:
   - `python scraper.py post-url total-load-more-click`
   - Replace the URL with your target post URL.
   - Example: `python scraper.py https://www.instagram.com/rohitsharma45/ 5`

7. Deactivate the virtual environment:
   - `deactivate`

## Based on
https://github.com/Ajit-Acharya/InstagramScrapper

This project draws inspiration from the InstagramScrapper repository by Ajit Acharya.

## License
This project is licensed under the [MIT License](https://github.com/AroldoGoulart/simple-instagram-comment-scrap/blob/main/LICENSE.md)