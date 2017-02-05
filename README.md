# titanic_challenge
Several statistics about the Titanic shipwreck


# Instructions:

Repo is in:

    https://github.com/jisazaTappsi/titanic_challenge

To run execute this command:

    ssh -i <private_key.txt> ubuntu@ec2-35-167-144-253.us-west-2.compute.amazonaws.com -t \
    "python titanic_challenge/main.py ~/titanic_challenge/titanicData.csv"

It will connect via ssh and execute the python program.

# Libraries Used:

## pandas

used extensively to import transform, filter and group data.


## kmodes

This library has kmodes algorithm to cluster records together according to similarities between them.
The difference between kmeans and kmodes is that the first one is used for numerical values while the second one for 
categorical values. For this particular problem the characteristics shared by a family (eg last_name, ticket, Cabin etc.)
happen to be all categorical. The "Fare" was the only numerical variable involved but switching to k-prototypes to
solve a mix type problem involved too much CPU power, as the number of clusters was high (230).

## Class and Sex Survival Probabilities

The results show a higher probability for first class followed by second class. This makes sense according to stories of the
shipwreck account. Also the female sex had a much higher probability than males this is also plausible according 
to those same stories.

## Find a family

For this exercise several characteristics (Cabin, LastName, Embarked, Pclass and Ticket) that families
share were input into a kmodes clustering algorithm. This algorithm grouped the individuals into 230 clusters or
possible families.

Then a second filter was applied to check for
1. clusters with more than 1 more member.
2. cabin sharing.
3. sharing last name.

After this filter 10 families are left. From those 10 families the biggest family is picked.

In practice there are 2 possible results the Fortune family and the Carter family for both cases the SibSp and Parch
fields were checked for consistency. The Carters are a typical family of 2 young parents and 2 children, while the 
Fortunes is a bigger family that although in this database has 4 members, seems to have 2 other members outside this DB.
This is plausible as the Titanic had 3000 passengers and we only have 891 in this set.


### kmodes explanation:

kmodes is similar to kmeans with the difference being that the first uses Hamming distance rather than the euclidean
distance. Also kmodes uses the mode(most frequent value in a set) to calculate the centroid rather than the mean and
the iteration process is a bit different.

### kmodes hyperparameter tunning

The parameters tuned on the kmodes model were:

1. number of clusters: This is analog to number of families. A sweet spot was found around 230 clusters that maximized
the number of families (at 43 families found) before strict filtering was applied which reduced the families to 10 or so.

2. init('Huang' or 'Cao'): Huang was chosen although similar performance (in terms of cost) was obtained with Cao.

3. n_init: Was left at the value of 5, as the random restarts didn't show much difference between them.
