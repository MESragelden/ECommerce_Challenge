# ECommerce_Challenge
<p>ECommerce_Challenge is a django Project, it hosts ECommerce application which connect to MongoDB on localhost 172.0.0.1 on port 27017
</p>

<h4>To run application</h4>
<h5> Make sure to install all needed package from 'requirement packages.txt'</h5>

```
cd ECommerce_Challenge
python .\manage.py makemigrations
python .\manage.py migrate
python .\manage.py runserver
```
<h4>To fill database browse to</h4>

```
http://127.0.0.1:8000/fill_database
```
<h4>To show all coffe machines browse to</h4>

```
http://127.0.0.1:8000/machines
```

<h4>To show all coffe pods browse to</h4>

```
http://127.0.0.1:8000/pods
```
<hr>
<h4> To filter machine try multiple options as follow

```
	http://127.0.0.1:8000/machines?name=CM001 
    http://127.0.0.1:8000/machines?product_type=base
	http://127.0.0.1:8000/machines?water_line_compatible=False
	http://127.0.0.1:8000/machines?size=small
```

<h5>You can make your own combination as below</h5>

```
    http://127.0.0.1:8000/machines?name=CM001&product_type=base model&water_line_compatible=False&size=small%20machine
```
<hr>
<h4> To filter coffe pods try multiple options as follow

```
	http://127.0.0.1:8000/pods?name=CP031
	http://127.0.0.1:8000/pods?product_type=small
	http://127.0.0.1:8000/pods?pack_size=1
	http://127.0.0.1:8000/pods?coffee_flavor=mocha
```

<h5>You can make your own combination as below</h5>

```
    http://127.0.0.1:8000/pods?name=CP031&product_type=small&pack_size=1&coffee_flavor=mocha
```