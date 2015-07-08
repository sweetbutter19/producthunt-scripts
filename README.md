# Product Hunt scripts
A set of scripts to play with Product Hunt API

Before starting to play, check that you have a token to use Product Hunt API and add it in `config.py`
No token yet ? Create your Application [here](https://www.producthunt.com/v1/oauth/applications/)

## Export votes in JSON file
File: `retrieve_votes.py`
* Parameter: Product ID
* Output: A JSON file `samples/votes_ID_product_name.json`

```
[
    {
        "nb_vote":1,
        "id_vote":1618984,
        "created_at":1434498740.0,
        "username":"clemkn"
    },
    {
        "nb_vote":2,
        "id_vote":1619032,
        "created_at":1434499275.0,
        "username":"xavierprosper"
    },
    {
        "nb_vote":3,
        "id_vote":1619144,
        "created_at":1434500291.0,
        "username":"bramk"
    }
]
```

### Some samples
* [Startup Stash](https://github.com/clemkn/product-hunt-scripts/blob/master/samples/votes_14717_startup_stash.json)
* [Captain](https://github.com/clemkn/product-hunt-scripts/blob/master/samples/votes_14929_captain.json)
* [Bookstck](https://github.com/clemkn/product-hunt-scripts/blob/master/samples/votes_24573_bookstck.json)

## Get the nb of posts, upvotes and the average of a hunter
File: `avg_hunter_votes.py`
* Parameter: Hunter username
* Output:
```
...
Yo 2.0 297
Top Startup Books 675
Bookstck 932
TawiPay 109
Crossroad 155
Readingstash 244
NewsBot 381
Email Hunter for Chrome 442
===========================
Details for clemkn
Nb of posts: 52 
Total of upvotes: 8935 
Average: 171
```
