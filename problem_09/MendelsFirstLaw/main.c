
#include <stdio.h>
#include <stdbool.h> 

typedef struct AllelType
{
    double amount;
    bool first;
    bool second;
} AllelType;

double chanceOfDominat(AllelType first, AllelType second) 
{
    double percent = 0.0;

    bool firstA = first.first;
    bool firstB = first.second;
    bool secondA = second.first;
    bool secondB = second.second;



    if (firstA || secondA)
        percent += .25;
    if(firstA || secondB)
        percent += .25;
    if(firstB || secondA)
        percent += .25;
    if(firstB || secondB)
        percent += .25;

    return percent;
}

int main()
{
    printf("Rosalind problem 09 - Mendel's first law\n");
    bool dominant = true, recessive = false;

    double dom = 21.0, hetzyg = 18.0, recess = 17.0;
    double total = dom + hetzyg + recess;

    //Allel* allelArray = malloc(total * sizeof(Allel*));
    AllelType allelArray[] = 
    { 
        {dom, dominant, dominant},
        {hetzyg, dominant, recessive},
        {recess, recessive, recessive},
    };

    double probablityOfDisDom = 0.0;


    //double matchItself = (2.0 / 6.0) * (1.0 / 5.0);
    //double matchOther  = (2.0 / 6.0) * (2.0 / 5.0);

    //double ans = (matchItself * 1.0) + (matchOther  * 1.0) + (matchOther  * 1.0) +
    //             (matchOther  * 1.0) + (matchItself * .75) + (matchOther  * .5) +
    //             (matchOther  * 1.0) + (matchOther  * .5)  + (matchItself * 0.0);

    for (int idx = 0; idx < sizeof(allelArray); idx++)
    {
        double probPicked = allelArray[idx].amount / total;
        for (int inneridx = 0; inneridx < sizeof(allelArray); inneridx++) 
        {
            double innerAmount = allelArray[inneridx].amount;
            
            if (idx == inneridx)
                innerAmount--;

            double innerProbPicked = innerAmount / (total - 1);

            double amountPercent = (probPicked * innerProbPicked) * chanceOfDominat(allelArray[idx], allelArray[inneridx]);

            probablityOfDisDom += amountPercent;
            
        }
    }

    printf("%lf", probablityOfDisDom);

    //struct allel allels[total];
}
