intro

The data contains ___ variables. The primary variables that deal with the question at hand are the Sales Method and the Revenue. 

The Sales Method indicates if the sale was made through email, through a phone call, it initiated through email and finalized through a phone call. Because of difference in spellings, some entries had to be changed to match the three categories. These were all clear-cut and easy to change. 

The revenue variable shows the amount made in a sale. Unfortunately, around 7.16% of the data is missing from this variable in the dataset. These




* Should I drop NaN, or fill na?
  * Did fillna
  * Try drop
    * Groupby sales_method, check for NaN 