<h1>Part one:scrapping images from the website</h1>
<h2>Introduce</h2>
If you would like to read Russian version of this state go <a href="https://github.com/Aleshka5/Test_Alex">there</a>.
<h2>First steps</h2>

I started by trying to parse website source with use the request library.
It was useless for two reasons:<br>
<ol>
<li> The website has dynamic HTML markup elements.</li>
<li> I couldn't use proxy with a request lib to get this website. (I can usually do this)</li>
</ol>
I have been use Selenium instead request with this regard.<br>

<h2>About parsing using the Selenium</h2>

I have had experience with the Selenium lib, but I have never used proxy
parameters for it. It is necessary, because the <a href="https://www.ralphlauren.nl/en/men/clothing/hoodies-sweatshirts/10204?webcat=men%7Cclothing%7Cmen-clothing-hoodies-sweatshirts">website</a> is banned in Russia. 

Unfortunately, free proxies are useless, because there are internet speed
is low. I rented my own IPv4 proxy server and it solved this problem. 

But I had new difficulties, so my new proxy had the necessary authenticated procedure.
It was truly hard to solve this problem myself, so I found answer on the StackOverflow.
I found this solution there and put it to a py module named "solve_authentication". 
Link to StackOverflow page is <a href="https://stackoverflow.com/questions/55582136/how-to-set-proxy-with-authentication-in-selenium-chromedriver-python">here</a>. 
It helped me connect to needed website quickly enough.

I understand how i can scrap all items from website, when I click to "View more".
I looked to the address bar and saw that: " ...&start=128&sz=6 ".
I find out that the start is - the start item index, and sz (size) is - the pagination size.<br>
Also I find out that the website has anti-parsing system. Some requests was reject with this regard.
Nevertheless I was able to increase number of successful connections. I made the requests at randomize 
time and always generated random headers.<br>  

<h2>About parsing HTML with BeautifulSoup</h2>

When I checked the HTML documents, I find that all needed images located in the tag "picture"
with an attribute named "tabindex", which has value equal "0".  

I find images of the people wearing a particular cloth and the cloth itself 
using the BeautifulSoup lib. However, images in a HTML documents located in the form of urls. 

<h2>About parsing images with using the Requests</h2>

In first, I create a request query to an url such as: <a href="https://www.rlmedia.io/is/image/PoloGSI/s7-1472168_alternate10?$plpDeskRFAlt$">https://www.rlmedia.io/is/image/PoloGSI/s7-1472168_alternate10?$plpDeskRFAlt$ </a>
Then I extracted  content from it.

When I tried to check images url, I found some identical images in pair. 
These images were locate in the end of Dataset and were named such as: "bad_image".  
Now I have dataset consisting of 122 correct image pairs.<br>
For example, it looks like this: <img src="https://github.com/Aleshka5/Test_Alex/blob/in_english/example_image_pair.JPG" width = 70%>

<h2>Part two</h2>

You can see my code solution, which solves part two <a href="https://colab.research.google.com/drive/1x0qdfwX699XY3XLNFwEMtXva4kffl3mZ?usp=sharing">here</a>.<br>
A little additional information about it.
Results:<img src="https://github.com/Aleshka5/Test_Alex/blob/in_english/example_image_preprocessing.png" width = 100%>  

<h2>Conclusion</h2> 
I done the task and translate my documentation on two languages. I am truly spent a lot of the project time to translate all this, because the main code was done about one day. It was an interesting experience. I am waiting for your feedback.
