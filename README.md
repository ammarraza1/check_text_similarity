Steps to run the docker container:

1. Clone the repository in your local drive using the following command: 
  git clone "https://github.com/ammarraza1/check_text_similarity.git"
2. Make sure you have docker installed on your machine. If not, select appropriate product to download from https://www.docker.com/products/docker-desktop
3. Build the docker image using the following command: 
  docker build -t webapp .
4. Run the docker container using the following command: 
  docker run -p 5000:5000 webapp
5. Open a web browswer in your local machine and open up localhost:5000
6. Make sure you input text in both the text boxes before pressing on the 'Check Similarity' button.
