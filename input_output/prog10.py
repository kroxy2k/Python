'''In a town, the percentage of men is 52. The percentage of total literacy is 48. If total percentage
of literate men is 35 of the total population, write a program to find the total number of
illiterate men and women if the population of the town is 80,000.'''
totpop= 80000

per_men = 52
per_litrcy = 48
pr_lit_men = 35

tot_men = (per_men / 100) * totpop
tot_wmn = totpop - tot_men

tot_litrte = (per_litrcy / 100) * totpop
lit_men = (pr_lit_men / 100) * totpop
lit_wmn = tot_litrte - lit_men
iltrt_men = tot_men - lit_men
iltrt_wmn = tot_wmn - lit_wmn

print("Total illiterate men:", int(iltrt_men))
print("Total illiterate women:", int(iltrt_wmn))
