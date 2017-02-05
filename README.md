# titanic_challenge
Several statistics about the Titanic shipwreck


# Libraries Used:


# pandas

used extensively to import transform, filter and group data.


# kmodes

Has kmodes algorithm to cluster records together according to similarities between them.
The difference between kmeans and kmodes is that the first one is used for numerical values while the second one for 
categorical values. For this particular problem the characteristics shared by a family (eg last_name, ticket, Cabin etc.)
happen to be all categorical. The "Fare" was the only numerical variable involved but switching to k-prototypes to
solve a mix type problem involved too much CPU power, as the number of clusters was high (230).

# kmodes explanation:

kmodes is similar to kmeans with the difference being that the first uses Hemming distance rather than the euclidean
distance. Also kmodes uses the mode(most frequent value in a set) to calculate the centroid rather than the mean and
the iteration process is a bit different.

# kmodes hyperparameter tunning

The parameters tuned on the kmodes model were:

1. number of clusters: This is analog to number of families. A sweet spot was found around 230 clusters that maximized
the number of families (at 43 families found) before strict filtering was applied which reduced the families to 10 or so.

2. init('Huang' or 'Cao'): Huang was chosen although similar performance (in terms of cost) was obtained with Cao.

3. n_init: Was left at the value of 5, as the random restarts didn't show much difference between them.
