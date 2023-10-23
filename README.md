# Project 2






<!-- TABLE OF CONTENTS -->
<details>
  <summary>Table of Contents</summary>
  <ol>
    <li>
      <a href="#about-the-project">About The Project</a>
      <ul>
        <li><a href="#built-with">Built With</a></li>
      </ul>
    </li>
    <li><a href="#project-tree">Project Tree</a></li>
    <li><a href="#installation">Installation</a></li>
  </ol>
</details>



<!-- ABOUT THE PROJECT -->
## About The Project

ELT pipeline which exctracts the realestate data from stie domiporta.pl and loads it to postgreSQL.Transofrmation part has been done in jupyter notebook where the raw data is being transformed to structured data frame by Pandas and and visualized in form of charts.

Project has been set on 3 Docker containers :

* Container with Scapy crawler built in python.
* Container with PostgreSQL
* Container with Jupyter Notebook



### Built With



[![My Skills](https://skills.thijs.gg/icons?i=py,docker,postgres)](https://skills.thijs.gg)

Python libraries used:

* scrapy
* psycopg2
* pandas



<p align="right">(<a href="#readme-top">back to top</a>)</p>

### Project Tree

<img width="318" alt="Zrzut ekranu 2023-01-17 o 20 50 05" src="https://user-images.githubusercontent.com/92937896/212997810-4e115a97-2f58-4b64-8a60-b405f55edd83.png">


### Installation


1. Create a file .env and save it in the root directory of the project.The file should contain following variables:
   ```sh
    POSTGRES_USER=
    POSTGRES_PASSWORD=
    POSTGRES_DB=
    TOKEN=
   ```

2. Clone the repo
   ```sh
   git clone
   ```
3. Go to main directory of the project
   ```sh
   cd projectname
   ```
4. Build the image of scraper by Dockerfile
   ```js
   cd realestate
   ```
   ```js
   docker build -t scraper_realestate . 
   ```
5. Build the image of jupyter notebook
   ```js
   cd notebook
   ```
   ```js
   docker build -t domiporta_notebook . 
   ```
6. Set the containers using docker compose file
   ```js
   cd projectname
   ```
   ```js
   docker compose up -d 
   ```

<p align="right">(<a href="#readme-top">back to top</a>)</p>

The scarper takes some time to crwal the data due to large number of requets beeing sent.
