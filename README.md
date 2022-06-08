
# Project Title

Stock-Movement-prediction-Using-Machine-Learning-Model-K-Means-Clustering

## Description
This Project proposes the use of machine learning techniques to evaluate stock market related data using the K-Means clustering algorithm. In addition, we are considering using data analysis and algorithmic trading strategies. In recent years, we have used machine learning to predict and investigate the behavior of various models. In this project, we will look at the stock market. The stock market is a non-linear, non-parametric system in nature and is very difficult to model with reasonable accuracy. Many investors are trying to find a way to predict stock prices.


## Getting Started

### Dataframe Implementation

* The necessary library ‘pandas’ and ‘numpy’ are imported to improvise the work in python 3. A dictionary ‘companies_dict’ is defined where ‘key’ is company’s name and ‘value’ is company’s stock code, 9 companies, 3 index and 3 commodities &currency are considered on there. Stock market data is extracted from yahoo finance, Onvista. The time period considered is from ‘2016–01–01’ to ‘2020–12–31’except Bitcoin-EUR. The stock movement of companies would be compared based on these 6 features column- ‘High’, ‘Low’, ‘Open’, ‘Close’, ‘Volume’, ‘Adj Close’. Data frame consist of two features of the dataset such as ‘Open’ and ‘Close’. The reason for choose these 2 features to identify the movements of the companies. ‘movement’ is defined as difference of opening and closing prices of a particular day.
* 


### Methodology

**K-means Clustering Algorithm

This project seeks to enhance and implement the algorithm (using scikit-learn library) proposed by using a more rigorous way of choosing the number of clusters K and predict the movements. To determine the effectiveness of companies' daily stock price movements are ran separately with implementing k-means model. K-means algorithm is used to optimize each cluster and ‘K-means++’ is used to find initial points. secondly, gather the remaining sample dots to their focal points in accordance with the criterion of minimum distance (Euclidean distance-), then we will get the initial classified cluster, and if the classification is unreasonable, we will modify it (calculate each cluster focal points again), iterate repetitively till we get a reasonable classification
**Vectorized backtesting

Vectorized backtesting is a powerful and efficient approach to backtesting the “pure” performance of a prediction-based algorithmic trading strategy. Hereby, we find out the return from the given features using numpy log and then the position represented as +1 or -1, are multiplied by the relevant log return.
We get algorithmic trading strategy mention ‘start_clus’. The possible result comes out since a long position earns the positive return and a short position earns the negative return of the several companies.
Summarize value of the return and the trading strategy shows up the final performance considering with or without trading cost. Several companies result outperform and underperform due to market volatility

### Analysis Final Performence

**Overview of portfolios

For simplicity, we refer to companies as its region name, for example, “Large Caps EUROPE” . With regards to large caps EUROPE portfolio, from 01.01.2017 to end of 2020, SAP is the best performer as it always tops the other two companies with ALV.DE being the worst performer.

**Result


![clustering](https://user-images.githubusercontent.com/81937480/172462288-5685a518-de1a-446c-ba68-1ca6e4b7dba4.png)
                                         Figure-1 : K-Means Cluster Scatter plot of Large Caps Europe.

**Explaination


Hereby, we show 3 companies cluster such as SAP, ALV.DE & AD.AS. we look into that all cluster are positive linear relationship which defines small value of x axis is correspond with small value of y axis and large value of x axis is correspond with large value of y axis. Here, X axis and Y axis show the normalize open and closing price value. The corresponding scatter cluster point show predicted position of those normalize value (1,-1) of each companies. The silhouette coefficient score for this cluster is 0.68, which is near to +1 . That means the clusters are almost well apart from each other and well separated from each point. The centroid show the imaginary or real location representing the center of the cluster. Every data point is allocated to each of the clusters through reducing the in-cluster sum of squares.



![without](https://user-images.githubusercontent.com/81937480/172464072-cceb66a1-c5af-43c2-a13d-130551af44fc.png)

**Evaluation


Company SAP and AD.AS shows the outperform then the market average return whereby (return<strat_clus).As an active investor we might buy the stocks and sell the stocks within short time period compared to the benchmark investor passively.on the other hand ALV.DE is shows the underperform (return>strat_clus) then comparative average returns.In this circumstances , an investor should buy the stock at lower price and hold it for long term until the price goes higher.


![with trade](https://user-images.githubusercontent.com/81937480/172503810-1aea9c52-fc2c-418a-9bfa-05188e01bde1.png)


**Evaluation


Consider trading cost as 100. Hereby its show the same results with a bit difference.SAP and AD.AS shows outperform as like previous. On the other side ALV.DE Show underperform here. Trading policy remain same here.


## Conclusion

In conclusion, The K-Means clustering algorithm can be thought of as Good because it gave great results. Still, some factors Affects the results of the dataset. The advantages of the K-Means clustering algorithm are easy to implement. Also, from the project we can adjusting and changing the number of clusters after normalized the data. The result of K-Means clustering is Used as a tool by educators and professional traders Reduce the risk factors of their investment. Machine learning will play a major role in the future Big data research because more methods and clusters are possible Implemented to improve the accuracy of the stock market Movement.

## Final Result

![Capture](https://user-images.githubusercontent.com/81937480/172504020-96eba4f9-c0ec-4b05-b14f-5ee472cfab8a.JPG)



## License

This project is licensed under the [NAME HERE] License - see the LICENSE.md file for details
