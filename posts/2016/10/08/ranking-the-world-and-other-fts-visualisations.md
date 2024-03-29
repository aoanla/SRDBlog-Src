<html><body><h1>Connectivity</h1>
More than a year ago, we published two articles [<strong><a href="https://www.scottishrollerderbyblog.com/posts/2015/06/07/visualising-the-internationalisation-of-roller-derby-part-1-of-2/">Pt1</a></strong>, <strong><a href="https://www.scottishrollerderbyblog.com/posts/2015/06/07/visualising-the-internationalisation-of-roller-derby-part-2-of-2-2011-to-present/">Pt2</a></strong>], using the <strong><a href="http://www.flattrackstats.com">Flat Track Stats</a></strong> dataset to visualise how Roller Derby has become both more International, but also, more importantly, more Connected over time.

We thought that it was a good time to revisit this, and see what 2016 looks like for international derby communities. With the <strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/03/16/the-japan-open-the-other-wftda-first-this-year/">Japan Open</a></strong>, and many big events in Europe, we expect to see that the connectivity of Women's Roller Derby in particular is increased.

In fact, the situation does seem similar to, but a little better, than 2015. Whilst there are 18 separate groups, all but one are pretty tiny (we show them in a slideshow below), consisting of only a few, mostly new, leagues each. As before, we are colour coding the nodes -<strong><span style="color:#ff0000;">Red is USA</span>, <span style="color:#0000ff;">Blue is Canada</span>,  <span style="color:#008000;">Green: Europe</span>, <span style="color:#00ffff;">Cyan: Australia</span>, <span style="color:#800080;">Purple: New Zealand</span>, <span style="color:#ffff00;">Yellow the Asia-Pacific</span>, </strong>and<strong> White: South America</strong>.

[gallery ids="9319,9320,9321,9322,9323,9324,9325,9326,9327,9328,9329,9330,9331,9332,9333,9334,9335" type="slideshow"]

By far the overwhelming majority of Women's Leagues are linked in the single largest Group, containing over 1200 teams!

<img class="alignnone size-full wp-image-9347" src="/2016/10/group-19.png" alt="group-1" width="5352" height="5352">

Men's Roller Derby is a surprisingly different matter. We see only three groups of Men's leagues in the FTS dataset... and each of them is significant and geographically localised. The largest represents North American Men's Derby, and the other two European and Pacific derby respectively - unlike Women's Roller Derby, there are no other isolated elements at all! (We expect that MRDA Champs will finally link the three groups, resulting in a single Group containing all of Men's Roller Derby, worldwide!)

[gallery ids="9350,9351,9352" type="slideshow"]

It's much less common, but Men's and Women's teams do play each other. If we rerun our connectivity analysis including bouts between gendered team classes, we find that something surprising happens: both North American and Pacific Men's Derby classes have links to the dominant group of Women's teams, but there's no such relationship between Men's European Derby.

As a result, out of the 19 Groups of connected leagues in the world, the largest is the majority of both men's and women's derby, and the second largest is the entirety of European Men's Roller Derby! This first, uber group is reproduced below:

<img class="alignnone size-full wp-image-9357" src="/2016/10/group-111.png" alt="group-1" width="5427" height="5427">

(We're a little perturbed by the lack of South American teams in the FTS dataset - obviously, we can only work with the data available to us, but as far as we can tell, no Men's South American teams did anything in 2016, according to FTS?)

<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/2/">On the next page</a></strong>, we'll do something else with this data...

<!--nextpage-->
<h1>Ranking</h1>
With such a large grouping, and an efficient rating scheme (as <strong><a href="https://aoanla.wordpress.com/2016/09/27/ranking-mechanisms-from-sport-and-roller-derby/">we wrote about here</a></strong>), we can finally compute something resembling the first "International" ranking for Roller Derby as a whole.

An immediate objection might be "but we already have the WFTDA Rankings (and they're making the algorithm better!)". We agree with <strong><a href="https://medium.com/thederbyapex/the-sept-30th-rankings-rundown-d5021d962b0#.e64gm9c0d">The Apex</a></strong>, that the recently released WFTDA Rankings are an improvement on previous rankings... but they still only, by design, rank WFTDA member leagues (and only their A Teams). The connected group of "rankable" teams includes many non WFTDA Members - either Women's leagues who have not joined WFTDA yet, B Teams of members, or even Men's leagues (who of course can't be WFTDA members).

Another objection might be: "but FlatTrackStats already does this (and this is all done with their data!)". We approve of everything FTS does as a service - which includes comprehensive statistical archiving, as well as their own ranking - but Flat Track Stats themselves also choose not to publish an "overall" ranking. You can see subsets of the ranking, for various sanctionings  (WFTDA, MRDA, UKRDA) - and various regions (Europe, Pacific etc) - but the underlying overall ranking for all teams is not available. Additionally, FTS has the opposite problem to WFTDA: because they're using Elo rankings, they try to rank everyone, even if a pair of teams have no competitors in common for more than a year! Our International Rankings explicitly only include the members of the largest connected set of teams in any given ranking period*, so no team can attain a rank without having played at least one bout to justify it.

This ranking, then, is based on our physical Spring optimiser, the best-in-class in our recent comprehensive review of predictive rankers. We rank the largest connected group on both score difference and (log) score ratio, and then compute a "synthetic" ranking by combining the normalised ranges of the two results. [This helps to compensate for the deficiencies of both metrics.]

So, the International Ranking (1 Oct 2016) is: (<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/3/">over the page</a></strong>, for length)

<!--nextpage-->

[<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/4/">CLICK HERE TO SKIP TO NEXT PAGE</a></strong>] [<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/6/">SKIP TO DISCUSSION</a></strong>]
<h2>SRD International Rankings 1 October 2016</h2>
<table>
<tbody>
<tr>
<td>RANK</td>
<td>Team</td>
<td>League</td>
<td>Type</td>
<td>Rating</td>
</tr>
<tr>
<td><b>1</b></td>
<td>Gotham Girls Roller Derby</td>
<td>Gotham</td>
<td>Womens</td>
<td>1.00000</td>
</tr>
<tr>
<td><b>2</b></td>
<td>Victorian Roller Derby League</td>
<td>Victoria</td>
<td>Womens</td>
<td>.96938</td>
</tr>
<tr>
<td><b>3</b></td>
<td>Saint Louis GateKeepers</td>
<td>St. Louis GateKeepers</td>
<td>Mens</td>
<td>.96254</td>
</tr>
<tr>
<td><b>4</b></td>
<td>Angel City Derby Girls</td>
<td>Angel City</td>
<td>Womens</td>
<td>.95143</td>
</tr>
<tr>
<td><b>5</b></td>
<td>London Rollergirls</td>
<td>London</td>
<td>Womens</td>
<td>.93049</td>
</tr>
<tr>
<td><b>6</b></td>
<td>Rose City Rollers</td>
<td>Rose</td>
<td>Womens</td>
<td>.92153</td>
</tr>
<tr>
<td><b>7</b></td>
<td>Texas Rollergirls</td>
<td>Texas</td>
<td>Womens</td>
<td>.91309</td>
</tr>
<tr>
<td><b>8</b></td>
<td>Your Mom Men's Roller Derby</td>
<td>Your Mom</td>
<td>Mens</td>
<td>.90259</td>
</tr>
<tr>
<td><b>9</b></td>
<td>New York Shock Exchange</td>
<td>Shock Exchange</td>
<td>Mens</td>
<td>.89790</td>
</tr>
<tr>
<td><b>10</b></td>
<td>Texas Men's Roller Derby</td>
<td>Texas Men's</td>
<td>Mens</td>
<td>.88954</td>
</tr>
<tr>
<td><b>11</b></td>
<td>Bridgetown Roller Derby</td>
<td>Bridgetown</td>
<td>Mens</td>
<td>.88487</td>
</tr>
<tr>
<td><b>12</b></td>
<td>Denver Roller Derby</td>
<td>Denver</td>
<td>Womens</td>
<td>.86656</td>
</tr>
<tr>
<td><b>13</b></td>
<td>Minnesota RollerGirls</td>
<td>Minnesota</td>
<td>Womens</td>
<td>.85927</td>
</tr>
<tr>
<td><b>14</b></td>
<td>Puget Sound Outcast Derby</td>
<td>Puget Sound</td>
<td>Mens</td>
<td>.85328</td>
</tr>
<tr>
<td><b>15</b></td>
<td>Arch Rival Roller Derby</td>
<td>Arch Rival</td>
<td>Womens</td>
<td>.85231</td>
</tr>
<tr>
<td><b>16</b></td>
<td>Jacksonville Roller Girls</td>
<td>Jacksonville</td>
<td>Womens</td>
<td>.85043</td>
</tr>
<tr>
<td><b>17</b></td>
<td>Atlanta Rollergirls</td>
<td>Atlanta</td>
<td>Womens</td>
<td>.84234</td>
</tr>
<tr>
<td><b>18</b></td>
<td>Rat City Roller Girls</td>
<td>Rat City</td>
<td>Womens</td>
<td>.83912</td>
</tr>
<tr>
<td><b>19</b></td>
<td>Tampa Roller Derby</td>
<td>Tampa</td>
<td>Womens</td>
<td>.82738</td>
</tr>
<tr>
<td><b>20</b></td>
<td>Crime City Rollers</td>
<td>Crime City</td>
<td>Womens</td>
<td>.82178</td>
</tr>
<tr>
<td><b>21</b></td>
<td>Magic City Misfits</td>
<td>Misfits</td>
<td>Mens</td>
<td>.82157</td>
</tr>
<tr>
<td><b>22</b></td>
<td>The Vancouver Murder</td>
<td>Vancouver Murder</td>
<td>Mens</td>
<td>.82022</td>
</tr>
<tr>
<td><b>23</b></td>
<td>Dallas Derby Devils</td>
<td>Dallas</td>
<td>Womens</td>
<td>.81959</td>
</tr>
<tr>
<td><b>24</b></td>
<td>Philly Roller Derby</td>
<td>Philly</td>
<td>Womens</td>
<td>.81896</td>
</tr>
<tr>
<td><b>25</b></td>
<td>Montreal Roller Derby</td>
<td>Montreal</td>
<td>Womens</td>
<td>.81175</td>
</tr>
<tr>
<td><b>26</b></td>
<td>Bay Area Derby</td>
<td>Bay Area</td>
<td>Womens</td>
<td>.80578</td>
</tr>
<tr>
<td><b>27</b></td>
<td>Terminal City Rollergirls</td>
<td>Terminal City</td>
<td>Womens</td>
<td>.79932</td>
</tr>
<tr>
<td><b>28</b></td>
<td>Team United Roller Derby</td>
<td>Team United</td>
<td>Womens</td>
<td>.79920</td>
</tr>
<tr>
<td><b>29</b></td>
<td>Detroit Derby Girls</td>
<td>Detroit</td>
<td>Womens</td>
<td>.79105</td>
</tr>
<tr>
<td><b>30</b></td>
<td>Victorian Vanguard</td>
<td>Vanguard</td>
<td>Mens</td>
<td>.78649</td>
</tr>
<tr>
<td><b>31</b></td>
<td>Rainy City Roller Derby</td>
<td>Rainy City (UK)</td>
<td>Womens</td>
<td>.78558</td>
</tr>
<tr>
<td><b>32</b></td>
<td>San Diego Aftershocks</td>
<td>Aftershocks</td>
<td>Mens</td>
<td>.78151</td>
</tr>
<tr>
<td><b>33</b></td>
<td>Mass Maelstrom Roller Derby</td>
<td>Mass Maelstrom</td>
<td>Mens</td>
<td>.78059</td>
</tr>
<tr>
<td><b>34</b></td>
<td>Sydney City SMASH Men's Roller Derby</td>
<td>Sydney City SMASH</td>
<td>Mens</td>
<td>.77455</td>
</tr>
<tr>
<td><b>35</b></td>
<td>Team Gold</td>
<td>Bay Area</td>
<td>Womens</td>
<td>.77162</td>
</tr>
<tr>
<td><b>36</b></td>
<td>Helsinki Roller Derby</td>
<td>Helsinki</td>
<td>Womens</td>
<td>.76742</td>
</tr>
<tr>
<td><b>37</b></td>
<td>Stockholm Roller Derby</td>
<td>Stockholm</td>
<td>Womens</td>
<td>.76490</td>
</tr>
<tr>
<td><b>38</b></td>
<td>Boston Roller Derby</td>
<td>Boston</td>
<td>Womens</td>
<td>.75800</td>
</tr>
<tr>
<td><b>39</b></td>
<td>Queen Bees</td>
<td>Victoria</td>
<td>Womens</td>
<td>.75495</td>
</tr>
<tr>
<td><b>40</b></td>
<td>Kallio Rolling Rainbow</td>
<td>Kallio</td>
<td>Womens</td>
<td>.75377</td>
</tr>
<tr>
<td><b>41</b></td>
<td>Philadelphia Hooligans</td>
<td>Philly Hooligans</td>
<td>Mens</td>
<td>.75245</td>
</tr>
<tr>
<td><b>42</b></td>
<td>Sun State Roller Girls</td>
<td>Sun State</td>
<td>Womens</td>
<td>.75199</td>
</tr>
<tr>
<td><b>43</b></td>
<td>Tasmania Men's Roller Derby</td>
<td>Tasmania Men's</td>
<td>Mens</td>
<td>.74989</td>
</tr>
<tr>
<td><b>44</b></td>
<td>ThunderQuads Roller Derby Masculino</td>
<td>ThunderQuads</td>
<td>Mens</td>
<td>.74784</td>
</tr>
<tr>
<td><b>45</b></td>
<td>Kinapori Fistfunkers</td>
<td>Kallio</td>
<td>Womens</td>
<td>.74133</td>
</tr>
<tr>
<td><b>46</b></td>
<td>Rocky Mountain Rollergirls</td>
<td>Rocky Mtn.</td>
<td>Womens</td>
<td>.74095</td>
</tr>
<tr>
<td><b>47</b></td>
<td>Dow Jones Average</td>
<td>Shock Exchange</td>
<td>Womens**</td>
<td>.73985</td>
</tr>
<tr>
<td><b>48</b></td>
<td>Santa Cruz Derby Girls</td>
<td>Santa Cruz</td>
<td>Womens</td>
<td>.73756</td>
</tr>
<tr>
<td><b>49</b></td>
<td>Roller Derby Toulouse (Women's)</td>
<td>Toulouse</td>
<td>Womens</td>
<td>.73601</td>
</tr>
<tr>
<td><b>50</b></td>
<td>Middlesbrough Milk Rollers</td>
<td>Middlesbrough</td>
<td>Womens</td>
<td>.73592</td>
</tr>
<tr>
<td><b>51</b></td>
<td>Bruising Altitude</td>
<td>Denver</td>
<td>Womens</td>
<td>.73527</td>
</tr>
<tr>
<td><b>52</b></td>
<td>Paris Rollergirls</td>
<td>Paris</td>
<td>Womens</td>
<td>.73371</td>
</tr>
<tr>
<td><b>53</b></td>
<td>Columbia QuadSquad Rollergirls</td>
<td>Columbia</td>
<td>Womens</td>
<td>.73112</td>
</tr>
<tr>
<td><b>54</b></td>
<td>Queen City Roller Girls</td>
<td>Queen City</td>
<td>Womens</td>
<td>.73006</td>
</tr>
<tr>
<td><b>55</b></td>
<td>Denver Roller Derby (Men's)</td>
<td>Ground Control</td>
<td>Mens</td>
<td>.72672</td>
</tr>
<tr>
<td><b>56</b></td>
<td>Arizona Roller Derby</td>
<td>Arizona</td>
<td>Womens</td>
<td>.72557</td>
</tr>
<tr>
<td><b>57</b></td>
<td>Sydney Roller Derby League</td>
<td>Sydney Assassins</td>
<td>Womens</td>
<td>.72393</td>
</tr>
<tr>
<td><b>58</b></td>
<td>Ohio Roller Derby</td>
<td>Ohio</td>
<td>Womens</td>
<td>.72335</td>
</tr>
<tr>
<td><b>59</b></td>
<td>Montreal Men's Roller Derby</td>
<td>Mont Royals</td>
<td>Mens</td>
<td>.72134</td>
</tr>
<tr>
<td><b>60</b></td>
<td>Steel City Roller Derby</td>
<td>Steel City</td>
<td>Womens</td>
<td>.72119</td>
</tr>
<tr>
<td><b>61</b></td>
<td>Wall Street Traitors</td>
<td>Gotham</td>
<td>Womens</td>
<td>.72090</td>
</tr>
<tr>
<td><b>62</b></td>
<td>Firing Squad (TX)</td>
<td>Texas</td>
<td>Womens</td>
<td>.72011</td>
</tr>
<tr>
<td><b>63</b></td>
<td>No Coast Derby Girls</td>
<td>No Coast</td>
<td>Womens</td>
<td>.71938</td>
</tr>
<tr>
<td><b>64</b></td>
<td>Charm City Roller Girls</td>
<td>Charm City</td>
<td>Womens</td>
<td>.71668</td>
</tr>
<tr>
<td><b>65</b></td>
<td>Varsity Derby League (Mens)</td>
<td>Capital Carnage</td>
<td>Mens</td>
<td>.71526</td>
</tr>
<tr>
<td><b>66</b></td>
<td>Mad Rollin' Dolls Roller Derby</td>
<td>Madison</td>
<td>Womens</td>
<td>.71483</td>
</tr>
<tr>
<td><b>67</b></td>
<td>Tampa Bay Men's Roller Derby</td>
<td>Tampa Bay</td>
<td>Mens</td>
<td>.71142</td>
</tr>
<tr>
<td><b>68</b></td>
<td>Axles of Annihilation</td>
<td>Rose</td>
<td>Womens</td>
<td>.71055</td>
</tr>
<tr>
<td><b>69</b></td>
<td>Windy City Rollers</td>
<td>Windy City</td>
<td>Womens</td>
<td>.70990</td>
</tr>
<tr>
<td><b>70</b></td>
<td>Perth Roller Derby</td>
<td>Perth</td>
<td>Womens</td>
<td>.70882</td>
</tr>
<tr>
<td><b>71</b></td>
<td>Ann Arbor Derby Dimes</td>
<td>Ann Arbor</td>
<td>Womens</td>
<td>.70793</td>
</tr>
<tr>
<td><b>72</b></td>
<td>Sacred City Derby Girls</td>
<td>Sacred</td>
<td>Womens</td>
<td>.70728</td>
</tr>
<tr>
<td><b>73</b></td>
<td>Lille Roller Girls</td>
<td>Lille</td>
<td>Womens</td>
<td>.70461</td>
</tr>
<tr>
<td><b>74</b></td>
<td>Calgary Roller Derby Association</td>
<td>Calgary</td>
<td>Womens</td>
<td>.70148</td>
</tr>
<tr>
<td><b>75</b></td>
<td>Brandywine Roller Derby</td>
<td>Brandywine</td>
<td>Womens</td>
<td>.70068</td>
</tr>
<tr>
<td><b>76</b></td>
<td>Naptown Roller Girls</td>
<td>Naptown</td>
<td>Womens</td>
<td>.70031</td>
</tr>
<tr>
<td><b>77</b></td>
<td>Tucson Roller Derby</td>
<td>Tucson</td>
<td>Womens</td>
<td>.69991</td>
</tr>
<tr>
<td><b>78</b></td>
<td>Charlottesville Derby Dames</td>
<td>Charlottesville</td>
<td>Womens</td>
<td>.69811</td>
</tr>
<tr>
<td><b>79</b></td>
<td>Orangeville Roller Girls</td>
<td>ORG All-Stars</td>
<td>Womens</td>
<td>.69779</td>
</tr>
<tr>
<td><b>80</b></td>
<td>Brisbane City-Rollers (Men's)</td>
<td>Brisbane Men's</td>
<td>Mens</td>
<td>.69639</td>
</tr>
<tr>
<td><b>81</b></td>
<td>Dock City Rollers</td>
<td>Dock City</td>
<td>Womens</td>
<td>.69598</td>
</tr>
<tr>
<td><b>82</b></td>
<td>Blue Ridge Rollergirls</td>
<td>Blue Ridge</td>
<td>Womens</td>
<td>.69433</td>
</tr>
<tr>
<td><b>83</b></td>
<td>Wheels of Mayhem</td>
<td>Wheels of Mayhem</td>
<td>Womens</td>
<td>.69425</td>
</tr>
<tr>
<td><b>84</b></td>
<td>Houston Roller Derby</td>
<td>Houston</td>
<td>Womens</td>
<td>.69303</td>
</tr>
<tr>
<td><b>85</b></td>
<td>Wasatch Roller Derby</td>
<td>Wasatch</td>
<td>Womens</td>
<td>.68927</td>
</tr>
<tr>
<td><b>86</b></td>
<td>Tiger Bay Brawlers</td>
<td>Tiger Bay</td>
<td>Womens</td>
<td>.68899</td>
</tr>
<tr>
<td><b>87</b></td>
<td>2x4 Roller Derby</td>
<td>2x4</td>
<td>Womens</td>
<td>.68665</td>
</tr>
<tr>
<td><b>88</b></td>
<td>Paradise City Roller Derby</td>
<td>Paradise City</td>
<td>Womens</td>
<td>.68649</td>
</tr>
<tr>
<td><b>89</b></td>
<td>Chinook City Roller Derby (Men's)</td>
<td>Reservoir Dogs</td>
<td>Mens</td>
<td>.68627</td>
</tr>
<tr>
<td><b>90</b></td>
<td>Canberra Roller Derby League</td>
<td>Canberra</td>
<td>Womens</td>
<td>.68405</td>
</tr>
<tr>
<td><b>91</b></td>
<td>Minnesota Men's Roller Derby</td>
<td>Twin Cities Terrors</td>
<td>Mens</td>
<td>.67988</td>
</tr>
<tr>
<td><b>92</b></td>
<td>Bruise Crew</td>
<td>Tampa</td>
<td>Womens</td>
<td>.67985</td>
</tr>
<tr>
<td><b>93</b></td>
<td>London Brawl Saints</td>
<td>London</td>
<td>Womens</td>
<td>.67908</td>
</tr>
<tr>
<td><b>94</b></td>
<td>Tweed Valley Roller's (Men's)</td>
<td>Tweed Valley Men's</td>
<td>Mens</td>
<td>.67746</td>
</tr>
<tr>
<td><b>95</b></td>
<td>Race City Rebels</td>
<td>Race City</td>
<td>Mens</td>
<td>.67632</td>
</tr>
<tr>
<td><b>96</b></td>
<td>Adelaide Roller Derby</td>
<td>Adeladies</td>
<td>Womens</td>
<td>.67534</td>
</tr>
<tr>
<td><b>97</b></td>
<td>Bear City Roller Derby</td>
<td>Bear City</td>
<td>Womens</td>
<td>.67390</td>
</tr>
<tr>
<td><b>98</b></td>
<td>Jet City Rollergirls</td>
<td>Jet City</td>
<td>Womens</td>
<td>.67269</td>
</tr>
<tr>
<td><b>99</b></td>
<td>Dublin Roller Derby</td>
<td>Dublin</td>
<td>Womens</td>
<td>.67085</td>
</tr>
<tr>
<td><b>100</b></td>
<td>Boulder County Bombers</td>
<td>Boulder County</td>
<td>Womens</td>
<td>.66812</td>
</tr>
<tr>
<td><b>101</b></td>
<td>Newcastle Roller Girls</td>
<td>Newcastle</td>
<td>Womens</td>
<td>.66733</td>
</tr>
<tr>
<td><b>102</b></td>
<td>Rage City Rollergirls</td>
<td>Rage City</td>
<td>Womens</td>
<td>.66601</td>
</tr>
<tr>
<td><b>103</b></td>
<td>Rocket Queens</td>
<td>Angel City</td>
<td>Womens</td>
<td>.66594</td>
</tr>
<tr>
<td><b>104</b></td>
<td>Nantes Derby Girls</td>
<td>Nantes</td>
<td>Womens</td>
<td>.66511</td>
</tr>
<tr>
<td><b>105</b></td>
<td>Nashville Rollergirls</td>
<td>Nashville</td>
<td>Womens</td>
<td>.66389</td>
</tr>
<tr>
<td><b>106</b></td>
<td>Tri-City Roller Derby</td>
<td>Tri-City</td>
<td>Womens</td>
<td>.66235</td>
</tr>
<tr>
<td><b>107</b></td>
<td>Auld Reekie Roller Girls</td>
<td>Auld Reekie</td>
<td>Womens</td>
<td>.65935</td>
</tr>
<tr>
<td><b>108</b></td>
<td>Dub City Derby Girls</td>
<td>Dub City</td>
<td>Womens</td>
<td>.65836</td>
</tr>
<tr>
<td><b>109</b></td>
<td>San Diego Roller Derby</td>
<td>San Diego Starlettes</td>
<td>Womens</td>
<td>.65733</td>
</tr>
<tr>
<td><b>110</b></td>
<td>Central City Roller Girls</td>
<td>Central City</td>
<td>Womens</td>
<td>.65727</td>
</tr>
<tr>
<td><b>111</b></td>
<td>Kansas City Roller Warriors</td>
<td>Kansas City</td>
<td>Womens</td>
<td>.65721</td>
</tr>
<tr>
<td><b>112</b></td>
<td>E-Ville Roller Derby</td>
<td>E-Ville</td>
<td>Womens</td>
<td>.65683</td>
</tr>
<tr>
<td><b>113</b></td>
<td>Drive-By City Rollers</td>
<td>Drive-By City</td>
<td>Mens</td>
<td>.65542</td>
</tr>
<tr>
<td><b>114</b></td>
<td>Western Australia Roller Derby</td>
<td>Western Australia</td>
<td>Womens</td>
<td>.65356</td>
</tr>
<tr>
<td><b>115</b></td>
<td>Bandoleras</td>
<td>Tucson</td>
<td>Womens</td>
<td>.65223</td>
</tr>
<tr>
<td><b>116</b></td>
<td>Dirty River Roller Grrrls</td>
<td>Dirty River</td>
<td>Womens</td>
<td>.65054</td>
</tr>
<tr>
<td><b>117</b></td>
<td>Oklahoma Victory Dolls</td>
<td>Okla. Victory</td>
<td>Womens</td>
<td>.64984</td>
</tr>
<tr>
<td><b>118</b></td>
<td>Rideau Valley Roller Girls</td>
<td>Rideau Valley</td>
<td>Womens</td>
<td>.64951</td>
</tr>
<tr>
<td><b>119</b></td>
<td>V Town Derby Dames</td>
<td>V Town</td>
<td>Womens</td>
<td>.64868</td>
</tr>
<tr>
<td><b>120</b></td>
<td>Light City Derby (Mens)</td>
<td>Light City</td>
<td>Mens</td>
<td>.64758</td>
</tr>
<tr>
<td><b>121</b></td>
<td>Sac City Rollers</td>
<td>Sac City</td>
<td>Womens</td>
<td>.64738</td>
</tr>
<tr>
<td><b>122</b></td>
<td>Copenhagen Roller Derby</td>
<td>Copenhagen</td>
<td>Womens</td>
<td>.64726</td>
</tr>
<tr>
<td><b>123</b></td>
<td>Nidaros Roller Derby</td>
<td>Nidaros</td>
<td>Womens</td>
<td>.64608</td>
</tr>
<tr>
<td><b>124</b></td>
<td>Collision Men's Derby</td>
<td>Collision</td>
<td>Mens</td>
<td>.64504</td>
</tr>
<tr>
<td><b>125</b></td>
<td>Rain of Terror</td>
<td>Rat City</td>
<td>Womens</td>
<td>.64488</td>
</tr>
<tr>
<td><b>126</b></td>
<td>Hot Wheel Roller Derby</td>
<td>Hot Wheel</td>
<td>Womens</td>
<td>.64428</td>
</tr>
<tr>
<td><b>127</b></td>
<td>Lane County Concussion</td>
<td>Lane County</td>
<td>Mens</td>
<td>.64417</td>
</tr>
<tr>
<td><b>128</b></td>
<td>Birmingham Blitz Dames</td>
<td>Blitz Dames</td>
<td>Womens</td>
<td>.64286</td>
</tr>
<tr>
<td><b>129</b></td>
<td>Capital District Men's Roller Derby</td>
<td>Trauma Authority</td>
<td>Mens</td>
<td>.64278</td>
</tr>
<tr>
<td><b>130</b></td>
<td>Sioux City Kornstalkers</td>
<td>Kornstalkers</td>
<td>Mens</td>
<td>.64228</td>
</tr>
<tr>
<td><b>131</b></td>
<td>Treasure Valley Roller Derby Inc.</td>
<td>Treasure Valley</td>
<td>Womens</td>
<td>.64160</td>
</tr>
<tr>
<td><b>132</b></td>
<td>Les Sexpos</td>
<td>Montreal</td>
<td>Womens</td>
<td>.63986</td>
</tr>
<tr>
<td><b>133</b></td>
<td>Rock City Riot</td>
<td>Rock City Riot</td>
<td>Mens</td>
<td>.63976</td>
</tr>
<tr>
<td><b>134</b></td>
<td>One Love Roller Dolls</td>
<td>Antwerp</td>
<td>Womens</td>
<td>.63877</td>
</tr>
<tr>
<td><b>135</b></td>
<td>Leeds Roller Dolls</td>
<td>Leeds</td>
<td>Womens</td>
<td>.63770</td>
</tr>
<tr>
<td><b>136</b></td>
<td>Rumble Bs</td>
<td>Atlanta</td>
<td>Womens</td>
<td>.63769</td>
</tr>
<tr>
<td><b>137</b></td>
<td>Perth Men's Derby</td>
<td>Perth Men's</td>
<td>Mens</td>
<td>.63760</td>
</tr>
<tr>
<td><b>138</b></td>
<td>Toronto Men's Roller Derby</td>
<td>Toronto Men's</td>
<td>Mens</td>
<td>.63674</td>
</tr>
<tr>
<td><b>139</b></td>
<td>Crime City B Team</td>
<td>Crime City</td>
<td>Womens</td>
<td>.63651</td>
</tr>
<tr>
<td><b>140</b></td>
<td>Motor City Disassembly Line</td>
<td>Detroit</td>
<td>Womens</td>
<td>.63598</td>
</tr>
<tr>
<td><b>141</b></td>
<td>Capital City Derby Dolls</td>
<td>Capital City</td>
<td>Womens</td>
<td>.63560</td>
</tr>
<tr>
<td><b>142</b></td>
<td>Helsinki Queen B’s</td>
<td>Helsinki</td>
<td>Womens</td>
<td>.63551</td>
</tr>
<tr>
<td><b>143</b></td>
<td>Granite City Roller Derby</td>
<td>Granite City</td>
<td>Womens</td>
<td>.63520</td>
</tr>
<tr>
<td><b>144</b></td>
<td>Cincinnati Rollergirls</td>
<td>Cincinnati</td>
<td>Womens</td>
<td>.63379</td>
</tr>
<tr>
<td><b>145</b></td>
<td>Brisbane City Rollers</td>
<td>Brisbane City</td>
<td>Womens</td>
<td>.63129</td>
</tr>
<tr>
<td><b>146</b></td>
<td>The Chicago Outfit Roller Derby</td>
<td>Chicago Outfit</td>
<td>Womens</td>
<td>.62964</td>
</tr>
<tr>
<td><b>147</b></td>
<td>Happy Valley Derby Darlins</td>
<td>Happy Valley</td>
<td>Womens</td>
<td>.62856</td>
</tr>
<tr>
<td><b>148</b></td>
<td>Omaha Rollergirls</td>
<td>Omaha</td>
<td>Womens</td>
<td>.62837</td>
</tr>
<tr>
<td><b>149</b></td>
<td>Undead Bettys Roller Derby</td>
<td>Undead Bettys</td>
<td>Womens</td>
<td>.62779</td>
</tr>
<tr>
<td><b>150</b></td>
<td>Bridgetown Brawlers</td>
<td>Bridgetown</td>
<td>Mens</td>
<td>.62702</td>
</tr>
<tr>
<td><b>151</b></td>
<td>Gent Go Go Roller Girls</td>
<td>Gent Go Go</td>
<td>Womens</td>
<td>.62625</td>
</tr>
<tr>
<td><b>152</b></td>
<td>Winnipeg Roller Derby League</td>
<td>Winnipeg</td>
<td>Womens</td>
<td>.62547</td>
</tr>
<tr>
<td><b>153</b></td>
<td>Saint Lunachix</td>
<td>Arch Rival</td>
<td>Womens</td>
<td>.62251</td>
</tr>
<tr>
<td><b>154</b></td>
<td>Mother State Roller Derby</td>
<td>Mother State</td>
<td>Womens</td>
<td>.62225</td>
</tr>
<tr>
<td><b>155</b></td>
<td>North Star Roller Girls</td>
<td>North Star</td>
<td>Womens</td>
<td>.62097</td>
</tr>
<tr>
<td><b>156</b></td>
<td>Carolina Wreckingballs Derby Team</td>
<td>Wreckingballs</td>
<td>Mens</td>
<td>.62066</td>
</tr>
<tr>
<td><b>157</b></td>
<td>Carolina Rollergirls</td>
<td>Carolina</td>
<td>Womens</td>
<td>.61999</td>
</tr>
<tr>
<td><b>158</b></td>
<td>Maine Roller Derby</td>
<td>Maine</td>
<td>Womens</td>
<td>.61940</td>
</tr>
<tr>
<td><b>159</b></td>
<td>Muddy River Rollers</td>
<td>Muddy River</td>
<td>Womens</td>
<td>.61877</td>
</tr>
<tr>
<td><b>160</b></td>
<td>Twin City Derby Girls</td>
<td>Twin City</td>
<td>Womens</td>
<td>.61664</td>
</tr>
<tr>
<td><b>161</b></td>
<td>Austin Anarchy Men's Roller Derby</td>
<td>Austin Anarchy</td>
<td>Mens</td>
<td>.61633</td>
</tr>
<tr>
<td><b>162</b></td>
<td>The Rolling Candies</td>
<td>Rolling Candies</td>
<td>Womens</td>
<td>.61494</td>
</tr>
<tr>
<td><b>163</b></td>
<td>San Fernando Valley Roller Derby</td>
<td>San Fernando</td>
<td>Womens</td>
<td>.61428</td>
</tr>
<tr>
<td><b>164</b></td>
<td>Grand Raggidy Roller Derby</td>
<td>Grand Raggidy</td>
<td>Womens</td>
<td>.61410</td>
</tr>
<tr>
<td><b>165</b></td>
<td>Gothenburg Roller Derby</td>
<td>Gothenburg</td>
<td>Womens</td>
<td>.61230</td>
</tr>
<tr>
<td><b>166</b></td>
<td>Mainland Misfits</td>
<td>Mainland Misfits</td>
<td>Womens</td>
<td>.61105</td>
</tr>
<tr>
<td><b>167</b></td>
<td>Sonoma County Roller Derby</td>
<td>Sonoma</td>
<td>Womens</td>
<td>.61076</td>
</tr>
<tr>
<td><b>168</b></td>
<td>Roller Derby Quebec</td>
<td>Quebec</td>
<td>Womens</td>
<td>.60993</td>
</tr>
<tr>
<td><b>169</b></td>
<td>Notorious V.I.Cs</td>
<td>Victoria</td>
<td>Womens</td>
<td>.60826</td>
</tr>
<tr>
<td><b>170</b></td>
<td>Amsterdam Roller Derby</td>
<td>Amsterdam</td>
<td>Womens</td>
<td>.60735</td>
</tr>
<tr>
<td><b>171</b></td>
<td>Pikes Peak Derby Dames</td>
<td>Pikes Peak</td>
<td>Womens</td>
<td>.60667</td>
</tr>
<tr>
<td><b>172</b></td>
<td>Bristol Roller Derby (Women's)</td>
<td>Bristol A</td>
<td>Womens</td>
<td>.60536</td>
</tr>
<tr>
<td><b>173</b></td>
<td>DC Rollergirls</td>
<td>DC</td>
<td>Womens</td>
<td>.60497</td>
</tr>
<tr>
<td><b>174</b></td>
<td>Milwaukee Blitzdkrieg</td>
<td>Blitzdkrieg</td>
<td>Mens</td>
<td>.60315</td>
</tr>
<tr>
<td><b>175</b></td>
<td>Bogota Bonebreakers</td>
<td>Bogota Bonebreakers</td>
<td>Womens</td>
<td>.60037</td>
</tr>
<tr>
<td><b>176</b></td>
<td>Ithaca League of Women Rollers</td>
<td>Ithaca</td>
<td>Womens</td>
<td>.59927</td>
</tr>
<tr>
<td><b>177</b></td>
<td>Cincinnati Battering Rams Men's Roller Derby</td>
<td>Battering Rams</td>
<td>Mens</td>
<td>.59863</td>
</tr>
<tr>
<td><b>178</b></td>
<td>Minnesota Nice</td>
<td>Minnesota</td>
<td>Womens</td>
<td>.59732</td>
</tr>
<tr>
<td><b>179</b></td>
<td>High Altitude Roller Derby</td>
<td>High Altitude</td>
<td>Womens</td>
<td>.59704</td>
</tr>
<tr>
<td><b>180</b></td>
<td>Oklahoma City Wolf Pack</td>
<td>OKC Wolf Pack</td>
<td>Mens</td>
<td>.59702</td>
</tr>
<tr>
<td><b>181</b></td>
<td>Battalion of Doom</td>
<td>Dallas</td>
<td>Womens</td>
<td>.59678</td>
</tr>
<tr>
<td><b>182</b></td>
<td>St. Pauli Roller Derby</td>
<td>St. Pauli</td>
<td>Womens</td>
<td>.59499</td>
</tr>
<tr>
<td><b>183</b></td>
<td>Tampere Roller Derby</td>
<td>Tampere</td>
<td>Womens</td>
<td>.59488</td>
</tr>
<tr>
<td><b>184</b></td>
<td>Berzerkers</td>
<td>Mass Maelstrom</td>
<td>Womens</td>
<td>.59463</td>
</tr>
<tr>
<td><b>185</b></td>
<td>Los Angeles Derby Dolls</td>
<td>LA Derby Dolls</td>
<td>Womens</td>
<td>.59252</td>
</tr>
<tr>
<td><b>186</b></td>
<td>Phoenix Rising</td>
<td>Arizona</td>
<td>Womens</td>
<td>.59155</td>
</tr>
<tr>
<td><b>187</b></td>
<td>Garden State Rollergirls</td>
<td>Garden State</td>
<td>Womens</td>
<td>.59148</td>
</tr>
<tr>
<td><b>188</b></td>
<td>Toronto Roller Derby</td>
<td>Toronto</td>
<td>Womens</td>
<td>.59139</td>
</tr>
<tr>
<td><b>189</b></td>
<td>Fort Myers Derby Girls</td>
<td>Ft. Myers</td>
<td>Womens</td>
<td>.59020</td>
</tr>
<tr>
<td><b>190</b></td>
<td>Emerald City Roller Derby</td>
<td>Emerald City</td>
<td>Womens</td>
<td>.58913</td>
</tr>
<tr>
<td><b>191</b></td>
<td>Monterey Bay Derby Dames</td>
<td>Monterey Bay</td>
<td>Womens</td>
<td>.58806</td>
</tr>
<tr>
<td><b>192</b></td>
<td>Gem City Rollergirls</td>
<td>Gem City</td>
<td>Womens</td>
<td>.58609</td>
</tr>
<tr>
<td><b>193</b></td>
<td>B-Keepers</td>
<td>St. Louis GateKeepers</td>
<td>Mens</td>
<td>.58600</td>
</tr>
<tr>
<td><b>194</b></td>
<td>Dairyland Doll B-team</td>
<td>Madison</td>
<td>Womens</td>
<td>.58597</td>
</tr>
<tr>
<td><b>195</b></td>
<td>SoCal Derby</td>
<td>SoCal</td>
<td>Womens</td>
<td>.58584</td>
</tr>
<tr>
<td><b>196</b></td>
<td>Pirate City Rollers</td>
<td>Pirate City</td>
<td>Womens</td>
<td>.58450</td>
</tr>
<tr>
<td><b>197</b></td>
<td>Blue Ribbon Bullies</td>
<td>Team United</td>
<td>Womens</td>
<td>.58341</td>
</tr>
<tr>
<td><b>198</b></td>
<td>Boston B Party</td>
<td>Boston</td>
<td>Womens</td>
<td>.58310</td>
</tr>
<tr>
<td><b>199</b></td>
<td>Richter City Roller Derby</td>
<td>Richter City</td>
<td>Womens</td>
<td>.58283</td>
</tr>
<tr>
<td><b>200</b></td>
<td>Saint Chux Derby Chix</td>
<td>St. Chux</td>
<td>Womens</td>
<td>.58168</td>
</tr>
<tr>
<td><b>201</b></td>
<td>Royal City Roller Girls</td>
<td>Royal City</td>
<td>Womens</td>
<td>.58146</td>
</tr>
<tr>
<td><b>202</b></td>
<td>BisMan Roller Derby (Men's)</td>
<td>Bomberz</td>
<td>Mens</td>
<td>.58093</td>
</tr>
<tr>
<td><b>203</b></td>
<td>Oslo Roller Derby</td>
<td>Oslo</td>
<td>Womens</td>
<td>.58068</td>
</tr>
<tr>
<td><b>204</b></td>
<td>Dublin Roller Derby B</td>
<td>Dublin</td>
<td>Womens</td>
<td>.57961</td>
</tr>
<tr>
<td><b>205</b></td>
<td>The Contenders</td>
<td>Rocky Mtn.</td>
<td>Womens</td>
<td>.57836</td>
</tr>
<tr>
<td><b>206</b></td>
<td>Swansea City Roller Derby</td>
<td>Swansea</td>
<td>Womens</td>
<td>.57834</td>
</tr>
<tr>
<td><b>207</b></td>
<td>Molly Roger Rollergirls</td>
<td>Molly Roger</td>
<td>Womens</td>
<td>.57817</td>
</tr>
<tr>
<td><b>208</b></td>
<td>Brussels Derby Pixies</td>
<td>Brussels (Womens)</td>
<td>Womens</td>
<td>.57654</td>
</tr>
<tr>
<td><b>209</b></td>
<td>Melbourne Northside Rollers</td>
<td>Melbourne Northside</td>
<td>Womens</td>
<td>.57598</td>
</tr>
<tr>
<td><b>210</b></td>
<td>Glasgow Roller Derby</td>
<td>Glasgow</td>
<td>Womens</td>
<td>.57597</td>
</tr>
<tr>
<td><b>211</b></td>
<td>Roller Derby Madrid</td>
<td>Madrid</td>
<td>Womens</td>
<td>.57549</td>
</tr>
<tr>
<td><b>212</b></td>
<td>Independence Dolls</td>
<td>Philly</td>
<td>Womens</td>
<td>.57509</td>
</tr>
<tr>
<td><b>213</b></td>
<td>Roller Derby Caen</td>
<td>Caen</td>
<td>Womens</td>
<td>.57473</td>
</tr>
<tr>
<td><b>214</b></td>
<td>Les Quedalles</td>
<td>Paris</td>
<td>Womens</td>
<td>.57449</td>
</tr>
<tr>
<td><b>215</b></td>
<td>Cheyenne Roller Derby</td>
<td>Capidoll Stars</td>
<td>Womens</td>
<td>.57418</td>
</tr>
<tr>
<td><b>216</b></td>
<td>Crossroads City Derby Girls</td>
<td>Crossroads City</td>
<td>Womens</td>
<td>.57411</td>
</tr>
<tr>
<td><b>217</b></td>
<td>Halifax Bruising Banditas</td>
<td>Banditas</td>
<td>Womens</td>
<td>.57395</td>
</tr>
<tr>
<td><b>218</b></td>
<td>Killamazoo Derby Darlins</td>
<td>Killamazoo</td>
<td>Womens</td>
<td>.57261</td>
</tr>
<tr>
<td><b>219</b></td>
<td>Brewcity Bruisers</td>
<td>Brewcity</td>
<td>Womens</td>
<td>.57095</td>
</tr>
<tr>
<td><b>220</b></td>
<td>Geelong Roller Derby League</td>
<td>Geelong</td>
<td>Womens</td>
<td>.57024</td>
</tr>
<tr>
<td><b>221</b></td>
<td>Mountain State Cutthroat Mafia</td>
<td>Uinta</td>
<td>Mens</td>
<td>.56953</td>
</tr>
<tr>
<td><b>222</b></td>
<td>Men's Ottawa Roller Derby</td>
<td>Slaughter Squad</td>
<td>Mens</td>
<td>.56943</td>
</tr>
<tr>
<td><b>223</b></td>
<td>Stuttgart Valley Rollergirls</td>
<td>Stuttgart Valley</td>
<td>Womens</td>
<td>.56941</td>
</tr>
<tr>
<td><b>224</b></td>
<td>Providence Roller Derby</td>
<td>Providence</td>
<td>Womens</td>
<td>.56927</td>
</tr>
<tr>
<td><b>225</b></td>
<td>Monterey Bay Derby Dames</td>
<td>Monterey Bay</td>
<td>Womens</td>
<td>.56905</td>
</tr>
<tr>
<td><b>226</b></td>
<td>Northwest Arkansas Roller Derby</td>
<td>NW Arkansas</td>
<td>Womens</td>
<td>.56870</td>
</tr>
<tr>
<td><b>227</b></td>
<td>Spa Town Roller Girls</td>
<td>Spa Town</td>
<td>Womens</td>
<td>.56802</td>
</tr>
<tr>
<td><b>228</b></td>
<td>Roc City Roller Derby</td>
<td>Roc City</td>
<td>Womens</td>
<td>.56757</td>
</tr>
<tr>
<td><b>229</b></td>
<td>Cape Fear Roller Girls</td>
<td>Cape Fear</td>
<td>Womens</td>
<td>.56577</td>
</tr>
<tr>
<td><b>230</b></td>
<td>Palouse River Rollers</td>
<td>Palouse</td>
<td>Womens</td>
<td>.56514</td>
</tr>
<tr>
<td><b>231</b></td>
<td>Beckley Area Derby Dames</td>
<td>Beckley</td>
<td>Womens</td>
<td>.56441</td>
</tr>
<tr>
<td><b>232</b></td>
<td>Arizona Men's Derby</td>
<td>Rattleskates</td>
<td>Mens</td>
<td>.56400</td>
</tr>
<tr>
<td><b>233</b></td>
<td>SAM Roller Derby (Women's)</td>
<td>All Blocks</td>
<td>Womens</td>
<td>.56382</td>
</tr>
<tr>
<td><b>234</b></td>
<td>Namur Roller Girls</td>
<td>Namur</td>
<td>Womens</td>
<td>.56296</td>
</tr>
<tr>
<td><b>235</b></td>
<td>Tender Hooligans</td>
<td>Rainy City (UK)</td>
<td>Womens</td>
<td>.56291</td>
</tr>
<tr>
<td><b>236</b></td>
<td>Fabulous Sin City Rollergirls</td>
<td>Sin City</td>
<td>Womens</td>
<td>.56256</td>
</tr>
<tr>
<td><b>237</b></td>
<td>Cambridge Rollerbillies</td>
<td>Cambridge</td>
<td>Womens</td>
<td>.56250</td>
</tr>
<tr>
<td><b>238</b></td>
<td>Rated PG Rollergirls</td>
<td>Northstar</td>
<td>Womens</td>
<td>.56195</td>
</tr>
<tr>
<td><b>239</b></td>
<td>Oulu Roller Derby</td>
<td>Oulu</td>
<td>Womens</td>
<td>.56132</td>
</tr>
<tr>
<td><b>240</b></td>
<td>London Rockin' Rollers</td>
<td>Rockin' Rollers</td>
<td>Womens</td>
<td>.56130</td>
</tr>
<tr>
<td><b>241</b></td>
<td>Long Island Roller Rebels</td>
<td>Long Island</td>
<td>Womens</td>
<td>.56109</td>
</tr>
<tr>
<td><b>242</b></td>
<td>Dead End Derby</td>
<td>Dead End</td>
<td>Womens</td>
<td>.56068</td>
</tr>
<tr>
<td><b>243</b></td>
<td>Nottingham Hellfire Harlots</td>
<td>Nottingham Hellfire Harlots</td>
<td>Womens</td>
<td>.55939</td>
</tr>
<tr>
<td><b>244</b></td>
<td>Lehigh Valley Rollergirls</td>
<td>Lehigh Valley</td>
<td>Womens</td>
<td>.55796</td>
</tr>
<tr>
<td><b>245</b></td>
<td>Royal Windsor Roller Girls</td>
<td>Royal Windsor</td>
<td>Womens</td>
<td>.55783</td>
</tr>
<tr>
<td><b>246</b></td>
<td>Silicon Valley Rollergirls</td>
<td>Silicon Valley</td>
<td>Womens</td>
<td>.55725</td>
</tr>
<tr>
<td><b>247</b></td>
<td>South Coast Roller Derby</td>
<td>South Coast</td>
<td>Womens</td>
<td>.55662</td>
</tr>
<tr>
<td><b>248</b></td>
<td>Granite State Roller Derby</td>
<td>Granite State</td>
<td>Womens</td>
<td>.55653</td>
</tr>
<tr>
<td><b>249</b></td>
<td>Norrköping Roller Derby</td>
<td>Norrköping</td>
<td>Womens</td>
<td>.55645</td>
</tr>
<tr>
<td><b>250</b></td>
<td>Fort Wayne Derby Girls</td>
<td>Ft. Wayne</td>
<td>Womens</td>
<td>.55552</td>
</tr>
<tr>
<td><b>251</b></td>
<td>Liverpool Roller Birds</td>
<td>Liverpool</td>
<td>Womens</td>
<td>.55478</td>
</tr>
<tr>
<td><b>252</b></td>
<td>Bakersfield Diamond Divas</td>
<td>Diamond Divas</td>
<td>Womens</td>
<td>.55379</td>
</tr>
<tr>
<td><b>253</b></td>
<td>Auckland Roller Derby League</td>
<td>Auckland</td>
<td>Womens</td>
<td>.55330</td>
</tr>
<tr>
<td><b>254</b></td>
<td>Sierra Regional Roller Derby</td>
<td>Sierra</td>
<td>Womens</td>
<td>.55253</td>
</tr>
<tr>
<td><b>255</b></td>
<td>Tenerife Roller Derby</td>
<td>Tenerife</td>
<td>Womens</td>
<td>.55251</td>
</tr>
<tr>
<td><b>256</b></td>
<td>Manchester Roller Derby (Women's)</td>
<td>Manchester</td>
<td>Womens</td>
<td>.55017</td>
</tr>
<tr>
<td><b>257</b></td>
<td>Eves of Destruction</td>
<td>Eves of Destruction</td>
<td>Womens</td>
<td>.54950</td>
</tr>
<tr>
<td><b>258</b></td>
<td>Junction City Roller Dolls</td>
<td>Junction City</td>
<td>Womens</td>
<td>.54918</td>
</tr>
<tr>
<td><b>259</b></td>
<td>Green Mountain Roller Derby</td>
<td>Green Mt.</td>
<td>Womens</td>
<td>.54810</td>
</tr>
<tr>
<td><b>260</b></td>
<td>Second Wind</td>
<td>Windy City</td>
<td>Womens</td>
<td>.54796</td>
</tr>
<tr>
<td><b>261</b></td>
<td>Les Quads de Paris Roller Derby</td>
<td>Quads de Paris</td>
<td>Womens</td>
<td>.54756</td>
</tr>
<tr>
<td><b>262</b></td>
<td>Big O Roller Bros</td>
<td>Big O</td>
<td>Mens</td>
<td>.54734</td>
</tr>
<tr>
<td><b>263</b></td>
<td>Bairn City Rollers (Women's)</td>
<td>Central Belters</td>
<td>Womens</td>
<td>.54635</td>
</tr>
<tr>
<td><b>264</b></td>
<td>Lansing Derby Vixens</td>
<td>Lansing Vixens</td>
<td>Womens</td>
<td>.54573</td>
</tr>
<tr>
<td><b>265</b></td>
<td>DuPage Derby Dames</td>
<td>DuPage Derby</td>
<td>Womens</td>
<td>.54553</td>
</tr>
<tr>
<td><b>266</b></td>
<td>London Batter C Power</td>
<td>London</td>
<td>Womens</td>
<td>.54491</td>
</tr>
<tr>
<td><b>267</b></td>
<td>South Sea Roller Derby</td>
<td>South Sea</td>
<td>Womens</td>
<td>.54470</td>
</tr>
<tr>
<td><b>268</b></td>
<td>Roller Derby Porto</td>
<td>Porto</td>
<td>Womens</td>
<td>.54403</td>
</tr>
<tr>
<td><b>269</b></td>
<td>Powder River Rousta Bout It Betties</td>
<td>Powder River</td>
<td>Womens</td>
<td>.54391</td>
</tr>
<tr>
<td><b>270</b></td>
<td>Roller Derby Dresden</td>
<td>Dresden</td>
<td>Womens</td>
<td>.54223</td>
</tr>
<tr>
<td><b>271</b></td>
<td>Warning Belles</td>
<td>Naptown</td>
<td>Womens</td>
<td>.53966</td>
</tr>
<tr>
<td><b>272</b></td>
<td>Hellgate Roller Derby</td>
<td>Hellgate</td>
<td>Womens</td>
<td>.53857</td>
</tr>
<tr>
<td><b>273</b></td>
<td>Pit Crew</td>
<td>Cherry City</td>
<td>Womens</td>
<td>.53853</td>
</tr>
<tr>
<td><b>274</b></td>
<td>Casco Bay Gentlemen's Derby</td>
<td>Casco Bay</td>
<td>Mens</td>
<td>.53769</td>
</tr>
<tr>
<td><b>275</b></td>
<td>Capital City Hooligans</td>
<td>Cap City Hooligans</td>
<td>Mens</td>
<td>.53767</td>
</tr>
<tr>
<td><b>276</b></td>
<td>Tiger Bay B-Bombs</td>
<td>Tiger Bay</td>
<td>Womens</td>
<td>.53746</td>
</tr>
<tr>
<td><b>277</b></td>
<td>Dominion Derby Girls</td>
<td>Dominion</td>
<td>Womens</td>
<td>.53739</td>
</tr>
<tr>
<td><b>278</b></td>
<td>Furness Firecrackers (Women's)</td>
<td>Furness Women's</td>
<td>Womens</td>
<td>.53705</td>
</tr>
<tr>
<td><b>279</b></td>
<td>Bay State Brawlers</td>
<td>Bay State Brawlers</td>
<td>Womens</td>
<td>.53702</td>
</tr>
<tr>
<td><b>280</b></td>
<td>South West Angels of Terror</td>
<td>Angels of Terror</td>
<td>Womens</td>
<td>.53682</td>
</tr>
<tr>
<td><b>281</b></td>
<td>Burning River Roller Derby</td>
<td>Burning River</td>
<td>Womens</td>
<td>.53629</td>
</tr>
<tr>
<td><b>282</b></td>
<td>ICT Roller Girls</td>
<td>ICT</td>
<td>Womens</td>
<td>.53600</td>
</tr>
<tr>
<td><b>283</b></td>
<td>Northern Brisbane Rollers</td>
<td>Northern Brisbane</td>
<td>Womens</td>
<td>.53568</td>
</tr>
<tr>
<td><b>284</b></td>
<td>Oklahoma City Roller Derby</td>
<td>Oklahoma City</td>
<td>Womens</td>
<td>.53490</td>
</tr>
<tr>
<td><b>285</b></td>
<td>Cornfed Derby Dames</td>
<td>Cornfed</td>
<td>Womens</td>
<td>.53347</td>
</tr>
<tr>
<td><b>286</b></td>
<td>Portsmouth Roller Wenches</td>
<td>Portsmouth</td>
<td>Womens</td>
<td>.53345</td>
</tr>
<tr>
<td><b>287</b></td>
<td>Central NY Roller Derby</td>
<td>Central NY</td>
<td>Womens</td>
<td>.53282</td>
</tr>
<tr>
<td><b>288</b></td>
<td>Limerick Roller Derby</td>
<td>Limerick</td>
<td>Womens</td>
<td>.53231</td>
</tr>
<tr>
<td><b>289</b></td>
<td>Rockcity Rollers</td>
<td>Rockcity</td>
<td>Womens</td>
<td>.53133</td>
</tr>
<tr>
<td><b>290</b></td>
<td>Bangor Roller Derby</td>
<td>Bangor</td>
<td>Womens</td>
<td>.53112</td>
</tr>
<tr>
<td><b>291</b></td>
<td>The Royal Swedish Roller Derby</td>
<td>The Royal Army</td>
<td>Womens</td>
<td>.53092</td>
</tr>
<tr>
<td><b>292</b></td>
<td>Gorge Roller Girls</td>
<td>Gorge Roller Girls</td>
<td>Womens</td>
<td>.53084</td>
</tr>
<tr>
<td><b>293</b></td>
<td>Salisbury Roller Girls</td>
<td>Salisbury</td>
<td>Womens</td>
<td>.53070</td>
</tr>
<tr>
<td><b>294</b></td>
<td>Darlings</td>
<td>V Town</td>
<td>Womens</td>
<td>.53065</td>
</tr>
<tr>
<td><b>295</b></td>
<td>Luleå Roller Derby</td>
<td>Luleå</td>
<td>Womens</td>
<td>.52965</td>
</tr>
<tr>
<td><b>296</b></td>
<td>Arbor Bruising Co.</td>
<td>Ann Arbor</td>
<td>Womens</td>
<td>.52953</td>
</tr>
<tr>
<td><b>297</b></td>
<td>Ventura County Derby Darlins</td>
<td>Ventura</td>
<td>Womens</td>
<td>.52942</td>
</tr>
<tr>
<td><b>298</b></td>
<td>SINtral Valley Derby Girls</td>
<td>SINtral Valley</td>
<td>Womens</td>
<td>.52805</td>
</tr>
<tr>
<td><b>299</b></td>
<td>Tallahassee Rollergirls</td>
<td>Tallahassee</td>
<td>Womens</td>
<td>.52584</td>
</tr>
<tr>
<td><b>300</b></td>
<td>Bleeding Heartland Roller Derby</td>
<td>Bleeding Heartland</td>
<td>Womens</td>
<td>.52579</td>
</tr>
<tr>
<td><b>301</b></td>
<td>Blocka Nostra</td>
<td>Toulouse</td>
<td>Womens</td>
<td>.52460</td>
</tr>
<tr>
<td><b>302</b></td>
<td>Downriver Roller Dolls</td>
<td>Downriver</td>
<td>Womens</td>
<td>.52448</td>
</tr>
<tr>
<td><b>303</b></td>
<td>10th Mountain Roller Dolls</td>
<td>10th Mtn.</td>
<td>Womens</td>
<td>.52387</td>
</tr>
<tr>
<td><b>304</b></td>
<td>Croydon Roller Derby</td>
<td>Croydon</td>
<td>Womens</td>
<td>.52364</td>
</tr>
<tr>
<td><b>305</b></td>
<td>Cherry City Derby Girls</td>
<td>Cherry City</td>
<td>Womens</td>
<td>.52300</td>
</tr>
<tr>
<td><b>306</b></td>
<td>Killer Bees</td>
<td>Sun State</td>
<td>Womens</td>
<td>.52292</td>
</tr>
<tr>
<td><b>307</b></td>
<td>Varsity Derby League</td>
<td>Varsity</td>
<td>Womens</td>
<td>.52260</td>
</tr>
<tr>
<td><b>308</b></td>
<td>Connecticut RollerGirls</td>
<td>Connecticut</td>
<td>Womens</td>
<td>.52259</td>
</tr>
<tr>
<td><b>309</b></td>
<td>Vienna Roller Derby</td>
<td>Vienna</td>
<td>Womens</td>
<td>.52250</td>
</tr>
<tr>
<td><b>310</b></td>
<td>Lava City Roller Dolls</td>
<td>Lava City</td>
<td>Womens</td>
<td>.52246</td>
</tr>
<tr>
<td><b>311</b></td>
<td>Folsom Prison Bruisers</td>
<td>Sac City</td>
<td>Womens</td>
<td>.52236</td>
</tr>
<tr>
<td><b>312</b></td>
<td>New Orleans Brass Roller Derby</td>
<td>New Orleans Brass</td>
<td>Mens</td>
<td>.52199</td>
</tr>
<tr>
<td><b>313</b></td>
<td>Wheat City Roller Derby</td>
<td>Wheat City</td>
<td>Womens</td>
<td>.52182</td>
</tr>
<tr>
<td><b>314</b></td>
<td>Dundee Roller Girls</td>
<td>Dundee</td>
<td>Womens</td>
<td>.52101</td>
</tr>
<tr>
<td><b>315</b></td>
<td>Little City Rollergirls</td>
<td>Little City</td>
<td>Womens</td>
<td>.52099</td>
</tr>
<tr>
<td><b>316</b></td>
<td>Chicago Bruise Brothers</td>
<td>Bruise Brothers</td>
<td>Mens</td>
<td>.52056</td>
</tr>
<tr>
<td><b>317</b></td>
<td>A-Stars B Team</td>
<td>Toronto</td>
<td>Womens</td>
<td>.52056</td>
</tr>
<tr>
<td><b>318</b></td>
<td>Newcastle Roller Derby League</td>
<td>Newcastle</td>
<td>Womens</td>
<td>.52011</td>
</tr>
<tr>
<td><b>319</b></td>
<td>Duke City Roller Derby</td>
<td>Duke</td>
<td>Womens</td>
<td>.51986</td>
</tr>
<tr>
<td><b>320</b></td>
<td>Inglorious Bombshells</td>
<td>Bear City</td>
<td>Womens</td>
<td>.51980</td>
</tr>
<tr>
<td><b>321</b></td>
<td>Snipers</td>
<td>Sydney Assassins</td>
<td>Womens</td>
<td>.51976</td>
</tr>
<tr>
<td><b>322</b></td>
<td>Gold Coast Derby Grrls</td>
<td>Gold Coast (FL)</td>
<td>Womens</td>
<td>.51927</td>
</tr>
<tr>
<td><b>323</b></td>
<td>Squamish Women's Roller Derby</td>
<td>Squamish</td>
<td>Womens</td>
<td>.51820</td>
</tr>
<tr>
<td><b>324</b></td>
<td>Red Stick Roller Derby</td>
<td>Red Stick</td>
<td>Womens</td>
<td>.51784</td>
</tr>
<tr>
<td><b>325</b></td>
<td>Shasta Roller Derby</td>
<td>Shasta</td>
<td>Womens</td>
<td>.51779</td>
</tr>
<tr>
<td><b>326</b></td>
<td>Lutece Destroyeuses Roller Derby Paris</td>
<td>Lutece</td>
<td>Womens</td>
<td>.51762</td>
</tr>
<tr>
<td><b>327</b></td>
<td>River City Rat Pack</td>
<td>Jacksonville</td>
<td>Womens</td>
<td>.51761</td>
</tr>
<tr>
<td><b>328</b></td>
<td>Rock Coast Rollers</td>
<td>Rock Coast</td>
<td>Womens</td>
<td>.51752</td>
</tr>
<tr>
<td><b>329</b></td>
<td>Dunedin Derby</td>
<td>Dunedin</td>
<td>Womens</td>
<td>.51696</td>
</tr>
<tr>
<td><b>330</b></td>
<td>Ark Valley High Rollers</td>
<td>Ark Valley</td>
<td>Womens</td>
<td>.51657</td>
</tr>
<tr>
<td><b>331</b></td>
<td>Big Easy Rollergirls</td>
<td>Big Easy</td>
<td>Womens</td>
<td>.51593</td>
</tr>
<tr>
<td><b>332</b></td>
<td>Coastal Assassins Roller Derby</td>
<td>Coastal Assassins</td>
<td>Womens</td>
<td>.51580</td>
</tr>
<tr>
<td><b>333</b></td>
<td>Naughty Pines Derby Dames</td>
<td>Naughty Pines</td>
<td>Womens</td>
<td>.51548</td>
</tr>
<tr>
<td><b>334</b></td>
<td>Rockin' City Rollergirls</td>
<td>Rockin' City</td>
<td>Womens</td>
<td>.51518</td>
</tr>
<tr>
<td><b>335</b></td>
<td>Terminal City B-Side</td>
<td>Terminal City</td>
<td>Womens</td>
<td>.51515</td>
</tr>
<tr>
<td><b>336</b></td>
<td>Bonneville Bone Crushers</td>
<td>Wasatch</td>
<td>Womens</td>
<td>.51505</td>
</tr>
<tr>
<td><b>337</b></td>
<td>Memphis Roller Derby</td>
<td>Memphis</td>
<td>Womens</td>
<td>.51503</td>
</tr>
<tr>
<td><b>338</b></td>
<td>Black Rose Rollers</td>
<td>Black Rose Rollers</td>
<td>Womens</td>
<td>.51418</td>
</tr>
<tr>
<td><b>339</b></td>
<td>Sitka Sound Slayers</td>
<td>Sitka</td>
<td>Womens</td>
<td>.51413</td>
</tr>
<tr>
<td><b>340</b></td>
<td>Brighton Rockers Roller Derby</td>
<td>Brighton (UK)</td>
<td>Womens</td>
<td>.51382</td>
</tr>
<tr>
<td><b>341</b></td>
<td>North Texas Roller Derby</td>
<td>North Texas</td>
<td>Womens</td>
<td>.51338</td>
</tr>
<tr>
<td><b>342</b></td>
<td>Roller Derby Rennes</td>
<td>Rennes</td>
<td>Womens</td>
<td>.51330</td>
</tr>
<tr>
<td><b>343</b></td>
<td>Standbys</td>
<td>Denver</td>
<td>Womens</td>
<td>.51300</td>
</tr>
<tr>
<td><b>344</b></td>
<td>Rock N Roller Queens</td>
<td>Rock N Roller Queens</td>
<td>Womens</td>
<td>.51283</td>
</tr>
<tr>
<td><b>345</b></td>
<td>Gallatin Roller Girlz</td>
<td>Gallatin Mayhem</td>
<td>Womens</td>
<td>.51269</td>
</tr>
<tr>
<td><b>346</b></td>
<td>KCRW Plan-B</td>
<td>Kansas City</td>
<td>Womens</td>
<td>.51247</td>
</tr>
<tr>
<td><b>347</b></td>
<td>Rainier Roller Girls</td>
<td>Rainier</td>
<td>Womens</td>
<td>.51240</td>
</tr>
<tr>
<td><b>348</b></td>
<td>Old Capitol City Roller Derby</td>
<td>Old Capitol City</td>
<td>Womens</td>
<td>.51186</td>
</tr>
<tr>
<td><b>349</b></td>
<td>Disciples</td>
<td>Sacred</td>
<td>Womens</td>
<td>.51185</td>
</tr>
<tr>
<td><b>350</b></td>
<td>Western MA Roller Derby</td>
<td>Western MA</td>
<td>Womens</td>
<td>.51143</td>
</tr>
<tr>
<td><b>351</b></td>
<td>Greenville Derby Dames</td>
<td>Greenville Derby Dames</td>
<td>Womens</td>
<td>.51097</td>
</tr>
<tr>
<td><b>352</b></td>
<td>Assassination City Roller Derby</td>
<td>Assassination</td>
<td>Womens</td>
<td>.51063</td>
</tr>
<tr>
<td><b>353</b></td>
<td>Unforgiven Roller Girls</td>
<td>Unforgiven</td>
<td>Womens</td>
<td>.51042</td>
</tr>
<tr>
<td><b>354</b></td>
<td>Northern Lights</td>
<td>North Star</td>
<td>Womens</td>
<td>.50997</td>
</tr>
<tr>
<td><b>355</b></td>
<td>Zurich City Rollergirlz</td>
<td>Zurich</td>
<td>Womens</td>
<td>.50977</td>
</tr>
<tr>
<td><b>356</b></td>
<td>Whakatane Roller Derby League</td>
<td>Whakatane</td>
<td>Womens</td>
<td>.50928</td>
</tr>
<tr>
<td><b>357</b></td>
<td>Jackson Hole Juggernauts</td>
<td>Juggernauts</td>
<td>Womens</td>
<td>.50921</td>
</tr>
<tr>
<td><b>358</b></td>
<td>Tri-City Plan B</td>
<td>Tri-City</td>
<td>Womens</td>
<td>.50885</td>
</tr>
<tr>
<td><b>359</b></td>
<td>Big Bucks High Rollers</td>
<td>High Rollers</td>
<td>Womens</td>
<td>.50870</td>
</tr>
<tr>
<td><b>360</b></td>
<td>Rising Rollers</td>
<td>Middlesbrough</td>
<td>Womens</td>
<td>.50857</td>
</tr>
<tr>
<td><b>361</b></td>
<td>Energetic City Roller Derby Association</td>
<td>Energetic City</td>
<td>Womens</td>
<td>.50827</td>
</tr>
<tr>
<td><b>362</b></td>
<td>Whippin' Hinnies</td>
<td>Newcastle</td>
<td>Womens</td>
<td>.50790</td>
</tr>
<tr>
<td><b>363</b></td>
<td>Bonnie Colliders</td>
<td>Dundee</td>
<td>Womens</td>
<td>.50780</td>
</tr>
<tr>
<td><b>364</b></td>
<td>Wirral Roller Derby</td>
<td>Wirral (Women's)</td>
<td>Womens</td>
<td>.50694</td>
</tr>
<tr>
<td><b>365</b></td>
<td>Sweetwater County Roller Derby</td>
<td>Bitter Sweet</td>
<td>Womens</td>
<td>.50641</td>
</tr>
<tr>
<td><b>366</b></td>
<td>Eastern Washington Wasteland Warriors</td>
<td>Eastern Washington</td>
<td>Mens</td>
<td>.50560</td>
</tr>
<tr>
<td><b>367</b></td>
<td>Lowcountry Highrollers</td>
<td>Lowcountry</td>
<td>Womens</td>
<td>.50556</td>
</tr>
<tr>
<td><b>368</b></td>
<td>Faultline Derby Devilz</td>
<td>Faultline</td>
<td>Womens</td>
<td>.50459</td>
</tr>
<tr>
<td><b>369</b></td>
<td>Orcet Roller Derby</td>
<td>Orcet (Womens)</td>
<td>Womens</td>
<td>.50437</td>
</tr>
<tr>
<td><b>370</b></td>
<td>Derby Revolution of Bakersfield</td>
<td>Bakersfield</td>
<td>Womens</td>
<td>.50294</td>
</tr>
<tr>
<td><b>371</b></td>
<td>Billings Roller Derby Dames</td>
<td>Billings</td>
<td>Womens</td>
<td>.50202</td>
</tr>
<tr>
<td><b>372</b></td>
<td>Derby City Roller Girls</td>
<td>Derby City</td>
<td>Womens</td>
<td>.50198</td>
</tr>
<tr>
<td><b>373</b></td>
<td>Appalachian Rollergirls</td>
<td>Appalachian Rollergirls</td>
<td>Womens</td>
<td>.50102</td>
</tr>
<tr>
<td><b>374</b></td>
<td>Humboldt Roller Derby</td>
<td>Humboldt</td>
<td>Womens</td>
<td>.50066</td>
</tr>
<tr>
<td><b>375</b></td>
<td>The Switchblade RollerGrrrls</td>
<td>Switchblade</td>
<td>Womens</td>
<td>.50056</td>
</tr>
<tr>
<td><b>376</b></td>
<td>Rogue Rollergirls</td>
<td>Rogue Rollergirls</td>
<td>Womens</td>
<td>.50032</td>
</tr>
<tr>
<td><b>377</b></td>
<td>Hammer City Roller Girls</td>
<td>Hammer City</td>
<td>Womens</td>
<td>.49998</td>
</tr>
<tr>
<td><b>378</b></td>
<td>Fernie Roller Derby League</td>
<td>Avalanche City</td>
<td>Womens</td>
<td>.49971</td>
</tr>
<tr>
<td><b>379</b></td>
<td>Capidolls</td>
<td>Capidoll Stars</td>
<td>Womens</td>
<td>.49861</td>
</tr>
<tr>
<td><b>380</b></td>
<td>Charlotte Roller Girls</td>
<td>Charlotte</td>
<td>Womens</td>
<td>.49783</td>
</tr>
<tr>
<td><b>381</b></td>
<td>Chinook City Roller Derby (Women's)</td>
<td>Chinook City</td>
<td>Womens</td>
<td>.49774</td>
</tr>
<tr>
<td><b>382</b></td>
<td>Atlanta Men's Roller Derby</td>
<td>Atlanta Men's</td>
<td>Mens</td>
<td>.49728</td>
</tr>
<tr>
<td><b>383</b></td>
<td>Chattanooga Roller Girls</td>
<td>Chattanooga</td>
<td>Womens</td>
<td>.49710</td>
</tr>
<tr>
<td><b>384</b></td>
<td>Road Warriors</td>
<td>No Coast</td>
<td>Womens</td>
<td>.49672</td>
</tr>
<tr>
<td><b>385</b></td>
<td>Detroit Men's Roller Derby</td>
<td>Detroit Riot</td>
<td>Mens</td>
<td>.49656</td>
</tr>
<tr>
<td><b>386</b></td>
<td>Spit Fires</td>
<td>Lava City</td>
<td>Womens</td>
<td>.49523</td>
</tr>
<tr>
<td><b>387</b></td>
<td>FoCo Roller Derby</td>
<td>FoCo</td>
<td>Womens</td>
<td>.49522</td>
</tr>
<tr>
<td><b>388</b></td>
<td>Dom City Dolls</td>
<td>Dom City</td>
<td>Womens</td>
<td>.49522</td>
</tr>
<tr>
<td><b>389</b></td>
<td>Wine Country Crushers</td>
<td>Wine Country</td>
<td>Womens</td>
<td>.49489</td>
</tr>
<tr>
<td><b>390</b></td>
<td>Quadfathers Men's Roller Derby</td>
<td>Quadfathers</td>
<td>Mens</td>
<td>.49449</td>
</tr>
<tr>
<td><b>391</b></td>
<td>Old Port Brigade</td>
<td>Maine</td>
<td>Womens</td>
<td>.49405</td>
</tr>
<tr>
<td><b>392</b></td>
<td>Tulsa Derby Militia</td>
<td>Tulsa Derby Militia</td>
<td>Mens</td>
<td>.49401</td>
</tr>
<tr>
<td><b>393</b></td>
<td>Barcelona Roller Derby</td>
<td>Barcelona</td>
<td>Womens</td>
<td>.49383</td>
</tr>
<tr>
<td><b>394</b></td>
<td>Classic City Rollergirls</td>
<td>Classic City</td>
<td>Womens</td>
<td>.49378</td>
</tr>
<tr>
<td><b>395</b></td>
<td>Fog City Rollers</td>
<td>Fog City</td>
<td>Womens</td>
<td>.49377</td>
</tr>
<tr>
<td><b>396</b></td>
<td>Blackpool Roller-Coasters</td>
<td>Blackpool</td>
<td>Womens</td>
<td>.49357</td>
</tr>
<tr>
<td><b>397</b></td>
<td>The Uppercuts</td>
<td>West Coast Knockouts</td>
<td>Womens</td>
<td>.49300</td>
</tr>
<tr>
<td><b>398</b></td>
<td>Heart Mountain Wreck on Wheels</td>
<td>Heart Mountain</td>
<td>Womens</td>
<td>.49291</td>
</tr>
<tr>
<td><b>399</b></td>
<td>Demolition City Roller Derby</td>
<td>Demolition</td>
<td>Womens</td>
<td>.49278</td>
</tr>
<tr>
<td><b>400</b></td>
<td>North Coast Nightmares</td>
<td>North Coast (BC)</td>
<td>Womens</td>
<td>.49223</td>
</tr>
<tr>
<td><b>401</b></td>
<td>All Star Reserves</td>
<td>Auld Reekie</td>
<td>Womens</td>
<td>.49204</td>
</tr>
<tr>
<td><b>402</b></td>
<td>Ruhrpott Roller Girls</td>
<td>Ruhrpott</td>
<td>Womens</td>
<td>.49105</td>
</tr>
<tr>
<td><b>403</b></td>
<td>Quad City Rollers</td>
<td>Quad City Rollers</td>
<td>Womens</td>
<td>.49078</td>
</tr>
<tr>
<td><b>404</b></td>
<td>Pittsburgh East Roller Villains (Men's)</td>
<td>Pittsburgh East (M)</td>
<td>Mens</td>
<td>.49028</td>
</tr>
<tr>
<td><b>405</b></td>
<td>Rotterdam Roller Derby</td>
<td>Rotterdam</td>
<td>Womens</td>
<td>.49019</td>
</tr>
<tr>
<td><b>406</b></td>
<td>North County Derby Alliance</td>
<td>North County</td>
<td>Womens</td>
<td>.48963</td>
</tr>
<tr>
<td><b>407</b></td>
<td>Shenanigans</td>
<td>Philly Hooligans</td>
<td>Mens</td>
<td>.48959</td>
</tr>
<tr>
<td><b>408</b></td>
<td>Tournament City Derby Dolls</td>
<td>Tournament City</td>
<td>Womens</td>
<td>.48888</td>
</tr>
<tr>
<td><b>409</b></td>
<td>The Cuttlefish</td>
<td>SoCal</td>
<td>Womens</td>
<td>.48879</td>
</tr>
<tr>
<td><b>410</b></td>
<td>Bullies</td>
<td>Hidden City</td>
<td>Womens</td>
<td>.48782</td>
</tr>
<tr>
<td><b>411</b></td>
<td>Magic City Rollers</td>
<td>Magic City Rollers</td>
<td>Womens</td>
<td>.48732</td>
</tr>
<tr>
<td><b>412</b></td>
<td>Derby Club le Cres Lattes Montpellier</td>
<td>Derby Club le Cres Lattes</td>
<td>Womens</td>
<td>.48706</td>
</tr>
<tr>
<td><b>413</b></td>
<td>Foothill Foxy Flyers</td>
<td>Foothill</td>
<td>Womens</td>
<td>.48672</td>
</tr>
<tr>
<td><b>414</b></td>
<td>All Star Rookies</td>
<td>Auld Reekie</td>
<td>Womens</td>
<td>.48609</td>
</tr>
<tr>
<td><b>415</b></td>
<td>Roller Derby Cáceres</td>
<td>Cáceres</td>
<td>Womens</td>
<td>.48596</td>
</tr>
<tr>
<td><b>416</b></td>
<td>Central Coast Roller Derby</td>
<td>Central Coast (CA)</td>
<td>Womens</td>
<td>.48564</td>
</tr>
<tr>
<td><b>417</b></td>
<td>Sioux City Roller Dames</td>
<td>Sioux City</td>
<td>Womens</td>
<td>.48511</td>
</tr>
<tr>
<td><b>418</b></td>
<td>Bandettes</td>
<td>San Diego Starlettes</td>
<td>Womens</td>
<td>.48497</td>
</tr>
<tr>
<td><b>419</b></td>
<td>Okanagan Roller Derby</td>
<td>Okanagan</td>
<td>Womens</td>
<td>.48462</td>
</tr>
<tr>
<td><b>420</b></td>
<td>Dark River Derby Coalition</td>
<td>Dark River</td>
<td>Womens</td>
<td>.48410</td>
</tr>
<tr>
<td><b>421</b></td>
<td>Hallam Hellcats Roller Derby</td>
<td>Hallam</td>
<td>Womens</td>
<td>.48397</td>
</tr>
<tr>
<td><b>422</b></td>
<td>Snake Pit Derby Dames</td>
<td>Snake Pit</td>
<td>Womens</td>
<td>.48378</td>
</tr>
<tr>
<td><b>423</b></td>
<td>Mass Attack Roller Derby</td>
<td>Mass Attack</td>
<td>Womens</td>
<td>.48369</td>
</tr>
<tr>
<td><b>424</b></td>
<td>Jane Deere</td>
<td>Calgary</td>
<td>Womens</td>
<td>.48342</td>
</tr>
<tr>
<td><b>425</b></td>
<td>Peach State Roller Derby</td>
<td>Peach State</td>
<td>Womens</td>
<td>.48310</td>
</tr>
<tr>
<td><b>426</b></td>
<td>Oxford Roller Derby</td>
<td>Oxford</td>
<td>Womens</td>
<td>.48285</td>
</tr>
<tr>
<td><b>427</b></td>
<td>South Side Derby Dolls</td>
<td>South Side (NSW)</td>
<td>Womens</td>
<td>.48253</td>
</tr>
<tr>
<td><b>428</b></td>
<td>Bellingham Roller Betties</td>
<td>Bellingham</td>
<td>Womens</td>
<td>.48251</td>
</tr>
<tr>
<td><b>429</b></td>
<td>Convict City Roller Derby</td>
<td>Convict City</td>
<td>Womens</td>
<td>.48181</td>
</tr>
<tr>
<td><b>430</b></td>
<td>Rated PG Rollergirls</td>
<td>Northstar</td>
<td>Womens</td>
<td>.48128</td>
</tr>
<tr>
<td><b>431</b></td>
<td>Bombshells</td>
<td>Boulder County</td>
<td>Womens</td>
<td>.48122</td>
</tr>
<tr>
<td><b>432</b></td>
<td>Alamo City Rollergirls</td>
<td>Alamo City</td>
<td>Womens</td>
<td>.48103</td>
</tr>
<tr>
<td><b>433</b></td>
<td>Harbour City Rollers</td>
<td>Harbour City Rollers</td>
<td>Womens</td>
<td>.48091</td>
</tr>
<tr>
<td><b>434</b></td>
<td>Road Ragers</td>
<td>Angel City</td>
<td>Womens</td>
<td>.48030</td>
</tr>
<tr>
<td><b>435</b></td>
<td>Battlestars</td>
<td>Brewcity</td>
<td>Womens</td>
<td>.48029</td>
</tr>
<tr>
<td><b>436</b></td>
<td>Rebellion Roller Derby</td>
<td>Rebellion</td>
<td>Womens</td>
<td>.47946</td>
</tr>
<tr>
<td><b>437</b></td>
<td>South Okanagan Roller Derby</td>
<td>Pistoleras</td>
<td>Womens</td>
<td>.47922</td>
</tr>
<tr>
<td><b>438</b></td>
<td>Roller Derby Panthers</td>
<td>Panthers Graou</td>
<td>Womens</td>
<td>.47894</td>
</tr>
<tr>
<td><b>439</b></td>
<td>Oxford Roller Derby B Team</td>
<td>Oxford</td>
<td>Womens</td>
<td>.47793</td>
</tr>
<tr>
<td><b>440</b></td>
<td>VCBs</td>
<td>Canberra</td>
<td>Womens</td>
<td>.47762</td>
</tr>
<tr>
<td><b>441</b></td>
<td>Sea Sirens</td>
<td>Tampa</td>
<td>Womens</td>
<td>.47759</td>
</tr>
<tr>
<td><b>442</b></td>
<td>Marseille Roller Derby Club (Women's)</td>
<td>Marseille</td>
<td>Womens</td>
<td>.47731</td>
</tr>
<tr>
<td><b>443</b></td>
<td>Harm City Men's Derby</td>
<td>Harm City</td>
<td>Mens</td>
<td>.47726</td>
</tr>
<tr>
<td><b>444</b></td>
<td>Brick City Bruisers</td>
<td>Garden State</td>
<td>Womens</td>
<td>.47712</td>
</tr>
<tr>
<td><b>445</b></td>
<td>Red Bluff Derby Girls</td>
<td>Red Bluff</td>
<td>Womens</td>
<td>.47680</td>
</tr>
<tr>
<td><b>446</b></td>
<td>River City Rollergirls</td>
<td>River City</td>
<td>Womens</td>
<td>.47616</td>
</tr>
<tr>
<td><b>447</b></td>
<td>Roller Derby Liège (Women's)</td>
<td>Liège (W)</td>
<td>Womens</td>
<td>.47609</td>
</tr>
<tr>
<td><b>448</b></td>
<td>Jersey Boys Roller Derby</td>
<td>Jersey Boys</td>
<td>Mens</td>
<td>.47591</td>
</tr>
<tr>
<td><b>449</b></td>
<td>Western Mass Destruction</td>
<td>Western Mass Destruction</td>
<td>Womens</td>
<td>.47571</td>
</tr>
<tr>
<td><b>450</b></td>
<td>Forest City Derby Girls</td>
<td>Forest City</td>
<td>Womens</td>
<td>.47562</td>
</tr>
<tr>
<td><b>451</b></td>
<td>Snake Pit Derby Dames</td>
<td>Snake Pit</td>
<td>Womens</td>
<td>.47509</td>
</tr>
<tr>
<td><b>452</b></td>
<td>Kent Roller Girls</td>
<td>Kent</td>
<td>Womens</td>
<td>.47487</td>
</tr>
<tr>
<td><b>453</b></td>
<td>ClarksVillain RollerGirls</td>
<td>ClarksVillains</td>
<td>Womens</td>
<td>.47469</td>
</tr>
<tr>
<td><b>454</b></td>
<td>Dirt City Roller Rats</td>
<td>Dirt City</td>
<td>Womens</td>
<td>.47462</td>
</tr>
<tr>
<td><b>455</b></td>
<td>NEO Roller Derby</td>
<td>NEO</td>
<td>Womens</td>
<td>.47269</td>
</tr>
<tr>
<td><b>456</b></td>
<td>Dixie Derby Girls</td>
<td>Dixie</td>
<td>Womens</td>
<td>.47254</td>
</tr>
<tr>
<td><b>457</b></td>
<td>High Tide Derby</td>
<td>High Tide</td>
<td>Womens</td>
<td>.47199</td>
</tr>
<tr>
<td><b>458</b></td>
<td>Saskatoon Roller Derby League</td>
<td>Saskatoon</td>
<td>Womens</td>
<td>.47128</td>
</tr>
<tr>
<td><b>459</b></td>
<td>Bay Rollers Roller Derby</td>
<td>Bay Rollers</td>
<td>Womens</td>
<td>.47121</td>
</tr>
<tr>
<td><b>460</b></td>
<td>Pile O' Bones Derby Club</td>
<td>Sugar Skulls</td>
<td>Womens</td>
<td>.47093</td>
</tr>
<tr>
<td><b>461</b></td>
<td>Harpies Roller Derby Milano</td>
<td>Milano</td>
<td>Womens</td>
<td>.47029</td>
</tr>
<tr>
<td><b>462</b></td>
<td>Wasteland Derby Dames</td>
<td>Wasteland</td>
<td>Womens</td>
<td>.46959</td>
</tr>
<tr>
<td><b>463</b></td>
<td>Mackay City Roller Maidens</td>
<td>Mackay City</td>
<td>Womens</td>
<td>.46939</td>
</tr>
<tr>
<td><b>464</b></td>
<td>A'Salt Creek Roller Girls</td>
<td>A'Salt Creek</td>
<td>Womens</td>
<td>.46850</td>
</tr>
<tr>
<td><b>465</b></td>
<td>Battlefords Roller Derby League</td>
<td>Battlefords</td>
<td>Womens</td>
<td>.46835</td>
</tr>
<tr>
<td><b>466</b></td>
<td>Radeladies</td>
<td>Adeladies</td>
<td>Womens</td>
<td>.46797</td>
</tr>
<tr>
<td><b>467</b></td>
<td>Sheffield Steel Rollergirls</td>
<td>Sheffield</td>
<td>Womens</td>
<td>.46788</td>
</tr>
<tr>
<td><b>468</b></td>
<td>Twin State Derby</td>
<td>Upper Valley</td>
<td>Womens</td>
<td>.46708</td>
</tr>
<tr>
<td><b>469</b></td>
<td>Wine Town Rollers</td>
<td>Wine Town</td>
<td>Womens</td>
<td>.46694</td>
</tr>
<tr>
<td><b>470</b></td>
<td>Reef City Rollergirls</td>
<td>Reef City</td>
<td>Womens</td>
<td>.46663</td>
</tr>
<tr>
<td><b>471</b></td>
<td>Lilac City Roller Girls</td>
<td>Lilac City</td>
<td>Womens</td>
<td>.46645</td>
</tr>
<tr>
<td><b>472</b></td>
<td>Anchor City Rollers</td>
<td>Halifax</td>
<td>Womens</td>
<td>.46630</td>
</tr>
<tr>
<td><b>473</b></td>
<td>Strong Island Derby Revolution</td>
<td>Strong Island</td>
<td>Womens</td>
<td>.46608</td>
</tr>
<tr>
<td><b>474</b></td>
<td>Les Divines Machines</td>
<td>Nantes</td>
<td>Womens</td>
<td>.46597</td>
</tr>
<tr>
<td><b>475</b></td>
<td>The Damned</td>
<td>Undead Bettys</td>
<td>Womens</td>
<td>.46567</td>
</tr>
<tr>
<td><b>476</b></td>
<td>Fox Cities Roller Derby</td>
<td>Fox Cities</td>
<td>Womens</td>
<td>.46557</td>
</tr>
<tr>
<td><b>477</b></td>
<td>Neath Port Talbot Roller Derby</td>
<td>Neath</td>
<td>Womens</td>
<td>.46470</td>
</tr>
<tr>
<td><b>478</b></td>
<td>Shore Points Roller Derby</td>
<td>Shore Points</td>
<td>Womens</td>
<td>.46333</td>
</tr>
<tr>
<td><b>479</b></td>
<td>Grunge City Rollers</td>
<td>Grunge City Elite</td>
<td>Womens</td>
<td>.46333</td>
</tr>
<tr>
<td><b>480</b></td>
<td>Greater Toronto Area Rollergirls</td>
<td>GTARollergirls</td>
<td>Womens</td>
<td>.46331</td>
</tr>
<tr>
<td><b>481</b></td>
<td>Willamette Kidney Thieves</td>
<td>Willamette</td>
<td>Womens</td>
<td>.46289</td>
</tr>
<tr>
<td><b>482</b></td>
<td>Greensboro Roller Derby</td>
<td>Greensboro</td>
<td>Womens</td>
<td>.46268</td>
</tr>
<tr>
<td><b>483</b></td>
<td>Dutchland Derby Rollers</td>
<td>Dutchland</td>
<td>Womens</td>
<td>.46247</td>
</tr>
<tr>
<td><b>484</b></td>
<td>KillaBytes</td>
<td>Silicon Valley</td>
<td>Womens</td>
<td>.46244</td>
</tr>
<tr>
<td><b>485</b></td>
<td>Rolling Hills Derby Dames</td>
<td>Rolling Hills</td>
<td>Womens</td>
<td>.46227</td>
</tr>
<tr>
<td><b>486</b></td>
<td>Roller Derby Metz Club</td>
<td>Metz</td>
<td>Womens</td>
<td>.46206</td>
</tr>
<tr>
<td><b>487</b></td>
<td>Dolly Rockit Rollers</td>
<td>Dolly Rockit</td>
<td>Womens</td>
<td>.46197</td>
</tr>
<tr>
<td><b>488</b></td>
<td>Cedar Valley Roller Derby</td>
<td>Cedar Valley</td>
<td>Womens</td>
<td>.46145</td>
</tr>
<tr>
<td><b>489</b></td>
<td>MOKAN Roller Girlz</td>
<td>MOKAN</td>
<td>Womens</td>
<td>.46143</td>
</tr>
<tr>
<td><b>490</b></td>
<td>Gang Green</td>
<td>Ohio</td>
<td>Womens</td>
<td>.46052</td>
</tr>
<tr>
<td><b>491</b></td>
<td>BSTRDs</td>
<td>Stockholm</td>
<td>Womens</td>
<td>.46037</td>
</tr>
<tr>
<td><b>492</b></td>
<td>Palm Coast Roller Derby</td>
<td>Palm Coast</td>
<td>Womens</td>
<td>.46006</td>
</tr>
<tr>
<td><b>493</b></td>
<td>Capital City Rollers</td>
<td>Capital City</td>
<td>Womens</td>
<td>.45999</td>
</tr>
<tr>
<td><b>494</b></td>
<td>Belfast Roller Derby</td>
<td>Belfast</td>
<td>Womens</td>
<td>.45907</td>
</tr>
<tr>
<td><b>495</b></td>
<td>NWO Roller Girls</td>
<td>NWO</td>
<td>Womens</td>
<td>.45883</td>
</tr>
<tr>
<td><b>496</b></td>
<td>Rum Rollers</td>
<td>Royal City</td>
<td>Womens</td>
<td>.45853</td>
</tr>
<tr>
<td><b>497</b></td>
<td>Juneau Roller Girls</td>
<td>Juneau</td>
<td>Womens</td>
<td>.45823</td>
</tr>
<tr>
<td><b>498</b></td>
<td>Tragic City Rollers</td>
<td>Tragic City</td>
<td>Womens</td>
<td>.45782</td>
</tr>
<tr>
<td><b>499</b></td>
<td>Hartford Area Roller Derby</td>
<td>Hartford Area</td>
<td>Womens</td>
<td>.45764</td>
</tr>
<tr>
<td><b>500</b></td>
<td>Cornwall Roller Derby</td>
<td>Cornwall</td>
<td>Womens</td>
<td>.45721</td>
</tr>
<tr>
<td><b>501</b></td>
<td>Hulls Angels Roller Dames</td>
<td>Hulls Angels</td>
<td>Womens</td>
<td>.45677</td>
</tr>
<tr>
<td><b>502</b></td>
<td>Swamp City Roller Rats</td>
<td>Swamp City</td>
<td>Womens</td>
<td>.45624</td>
</tr>
<tr>
<td><b>503</b></td>
<td>Les Sales Gosses</td>
<td>Sales Gosses</td>
<td>Womens</td>
<td>.45601</td>
</tr>
<tr>
<td><b>504</b></td>
<td>Munich Rolling Rebels</td>
<td>Munich</td>
<td>Womens</td>
<td>.45568</td>
</tr>
<tr>
<td><b>505</b></td>
<td>Wine Country Homewreckers</td>
<td>Sonoma</td>
<td>Womens</td>
<td>.45522</td>
</tr>
<tr>
<td><b>506</b></td>
<td>Killjoys</td>
<td>Killjoys</td>
<td>Womens</td>
<td>.45519</td>
</tr>
<tr>
<td><b>507</b></td>
<td>Ingles de Acero B</td>
<td>Barcelona</td>
<td>Womens</td>
<td>.45517</td>
</tr>
<tr>
<td><b>508</b></td>
<td>Grande Prairie Roller Derby</td>
<td>Grande Prairie</td>
<td>Womens</td>
<td>.45460</td>
</tr>
<tr>
<td><b>509</b></td>
<td>Steel Beamers</td>
<td>Steel City</td>
<td>Womens</td>
<td>.45417</td>
</tr>
<tr>
<td><b>510</b></td>
<td>Iron Range Maidens</td>
<td>Iron Range</td>
<td>Womens</td>
<td>.45381</td>
</tr>
<tr>
<td><b>511</b></td>
<td>Violent Lambs</td>
<td>Cincinnati</td>
<td>Womens</td>
<td>.45379</td>
</tr>
<tr>
<td><b>512</b></td>
<td>Rawlins Pen-Up Girlz</td>
<td>Rawlins</td>
<td>Womens</td>
<td>.45300</td>
</tr>
<tr>
<td><b>513</b></td>
<td>Palouse River Rampage</td>
<td>Palouse</td>
<td>Womens</td>
<td>.45290</td>
</tr>
<tr>
<td><b>514</b></td>
<td>Rubber City Rollergirls</td>
<td>Rubber City</td>
<td>Womens</td>
<td>.45271</td>
</tr>
<tr>
<td><b>515</b></td>
<td>Magic City Rollers B Team</td>
<td>Magic City Rollers</td>
<td>Womens</td>
<td>.45260</td>
</tr>
<tr>
<td><b>516</b></td>
<td>Bombshell Brawlers</td>
<td>Winnipeg</td>
<td>Womens</td>
<td>.45233</td>
</tr>
<tr>
<td><b>517</b></td>
<td>Muscogee Roller Girls</td>
<td>Muscogee</td>
<td>Womens</td>
<td>.45169</td>
</tr>
<tr>
<td><b>518</b></td>
<td>Resurrection Roller Girls</td>
<td>Resurrection</td>
<td>Womens</td>
<td>.45102</td>
</tr>
<tr>
<td><b>519</b></td>
<td>Norfolk Roller Derby</td>
<td>Norfolk</td>
<td>Womens</td>
<td>.45060</td>
</tr>
<tr>
<td><b>520</b></td>
<td>Cannie Gingers</td>
<td>Glasgow</td>
<td>Womens</td>
<td>.45048</td>
</tr>
<tr>
<td><b>521</b></td>
<td>Oil City Derby Girls</td>
<td>Oil City</td>
<td>Womens</td>
<td>.45039</td>
</tr>
<tr>
<td><b>522</b></td>
<td>Jukes of Hazzard</td>
<td>Atlanta</td>
<td>Womens</td>
<td>.45018</td>
</tr>
<tr>
<td><b>523</b></td>
<td>Hard Knox Roller Girls</td>
<td>Hard Knox</td>
<td>Womens</td>
<td>.45009</td>
</tr>
<tr>
<td><b>524</b></td>
<td>Kokeshi Rollerdolls</td>
<td>Kokeshi Rollerdolls</td>
<td>Womens</td>
<td>.44997</td>
</tr>
<tr>
<td><b>525</b></td>
<td>Kings County Derby Queens</td>
<td>Hooligans</td>
<td>Womens</td>
<td>.44875</td>
</tr>
<tr>
<td><b>526</b></td>
<td>Capitol Offenders</td>
<td>DC</td>
<td>Womens</td>
<td>.44863</td>
</tr>
<tr>
<td><b>527</b></td>
<td>Gas City Roller Derby Association (Women)</td>
<td>Gas City</td>
<td>Womens</td>
<td>.44795</td>
</tr>
<tr>
<td><b>528</b></td>
<td>National Maulers</td>
<td>DC</td>
<td>Womens</td>
<td>.44784</td>
</tr>
<tr>
<td><b>529</b></td>
<td>Prairieland Punishers Roller Derby</td>
<td>Punishers</td>
<td>Womens</td>
<td>.44744</td>
</tr>
<tr>
<td><b>530</b></td>
<td>Music City Brawl Stars</td>
<td>Nashville</td>
<td>Womens</td>
<td>.44716</td>
</tr>
<tr>
<td><b>531</b></td>
<td>Suburbia Roller Derby</td>
<td>Suburbia</td>
<td>Womens</td>
<td>.44708</td>
</tr>
<tr>
<td><b>532</b></td>
<td>Star City Roller Girls</td>
<td>Star City</td>
<td>Womens</td>
<td>.44698</td>
</tr>
<tr>
<td><b>533</b></td>
<td>Smokin' Laces</td>
<td>Mainland Misfits</td>
<td>Womens</td>
<td>.44692</td>
</tr>
<tr>
<td><b>534</b></td>
<td>Cleveland Men's Roller Derby</td>
<td>Cleveland Men's</td>
<td>Mens</td>
<td>.44680</td>
</tr>
<tr>
<td><b>535</b></td>
<td>Gas City Rollers</td>
<td>Gas City</td>
<td>Womens</td>
<td>.44615</td>
</tr>
<tr>
<td><b>536</b></td>
<td>Cologne Roller Derby</td>
<td>Cologne</td>
<td>Womens</td>
<td>.44560</td>
</tr>
<tr>
<td><b>537</b></td>
<td>Gold Pain City Derby Girls</td>
<td>Gold Pain</td>
<td>Womens</td>
<td>.44519</td>
</tr>
<tr>
<td><b>538</b></td>
<td>Continental Dividers</td>
<td>Ark Valley</td>
<td>Womens</td>
<td>.44518</td>
</tr>
<tr>
<td><b>539</b></td>
<td>Whip-Its</td>
<td>Leeds</td>
<td>Womens</td>
<td>.44515</td>
</tr>
<tr>
<td><b>540</b></td>
<td>Aftershocks</td>
<td>Peninsula</td>
<td>Womens</td>
<td>.44488</td>
</tr>
<tr>
<td><b>541</b></td>
<td>Central Ohio Roller Derby</td>
<td>Central Ohio</td>
<td>Womens</td>
<td>.44414</td>
</tr>
<tr>
<td><b>542</b></td>
<td>Peninsula Roller Girls</td>
<td>Peninsula</td>
<td>Womens</td>
<td>.44407</td>
</tr>
<tr>
<td><b>543</b></td>
<td>Slamazons</td>
<td>Pikes Peak</td>
<td>Womens</td>
<td>.44376</td>
</tr>
<tr>
<td><b>544</b></td>
<td>CoMo Derby Dames</td>
<td>CoMo</td>
<td>Womens</td>
<td>.44346</td>
</tr>
<tr>
<td><b>545</b></td>
<td>Pacific Coast Recycled Rollers</td>
<td>Recycled Rollers</td>
<td>Womens</td>
<td>.44281</td>
</tr>
<tr>
<td><b>546</b></td>
<td>Joint Base Lewis-McChord Bettie Brigade</td>
<td>Bettie Brigade</td>
<td>Womens</td>
<td>.44280</td>
</tr>
<tr>
<td><b>547</b></td>
<td>Hertfordshire Roller Derby</td>
<td>Hell's Belles</td>
<td>Womens</td>
<td>.44225</td>
</tr>
<tr>
<td><b>548</b></td>
<td>Killer Rollbots</td>
<td>Rollbots</td>
<td>Womens</td>
<td>.44216</td>
</tr>
<tr>
<td><b>549</b></td>
<td>Capital City Crushers</td>
<td>Crushers</td>
<td>Womens</td>
<td>.44214</td>
</tr>
<tr>
<td><b>550</b></td>
<td>Richland County Regulators Derby Team</td>
<td>Richland County Regulators</td>
<td>Womens</td>
<td>.44201</td>
</tr>
<tr>
<td><b>551</b></td>
<td>Tokyo Roller Girls</td>
<td>Tokyo</td>
<td>Womens</td>
<td>.44184</td>
</tr>
<tr>
<td><b>552</b></td>
<td>Borderland Brawlers Roller Derby</td>
<td>Borderland Brawlers</td>
<td>Womens</td>
<td>.44159</td>
</tr>
<tr>
<td><b>553</b></td>
<td>Roller Girls of the Apocalypse</td>
<td>RGA The Wreckoning</td>
<td>Womens</td>
<td>.44126</td>
</tr>
<tr>
<td><b>554</b></td>
<td>Portneuf Valley Bruisers</td>
<td>Portneuf</td>
<td>Womens</td>
<td>.44098</td>
</tr>
<tr>
<td><b>555</b></td>
<td>Kouvola Rock N Rollers</td>
<td>Kouvola</td>
<td>Womens</td>
<td>.44069</td>
</tr>
<tr>
<td><b>556</b></td>
<td>Sunshine Coast Roller Girls</td>
<td>Sunshine Coast</td>
<td>Womens</td>
<td>.44055</td>
</tr>
<tr>
<td><b>557</b></td>
<td>Storm City Roller Girls</td>
<td>Storm City</td>
<td>Womens</td>
<td>.43993</td>
</tr>
<tr>
<td><b>558</b></td>
<td>Prague City Roller Derby</td>
<td>Prague</td>
<td>Womens</td>
<td>.43985</td>
</tr>
<tr>
<td><b>559</b></td>
<td>Hell's Ass Derby Girls</td>
<td>Strasbourg</td>
<td>Womens</td>
<td>.43942</td>
</tr>
<tr>
<td><b>560</b></td>
<td>Blitz</td>
<td>Dutchland</td>
<td>Womens</td>
<td>.43928</td>
</tr>
<tr>
<td><b>561</b></td>
<td>Heartland Hellcats</td>
<td>N. Platte</td>
<td>Womens</td>
<td>.43859</td>
</tr>
<tr>
<td><b>562</b></td>
<td>Living Dead</td>
<td>E-Ville</td>
<td>Womens</td>
<td>.43852</td>
</tr>
<tr>
<td><b>563</b></td>
<td>Jersey Shore Roller Girls</td>
<td>Jersey Shore</td>
<td>Womens</td>
<td>.43810</td>
</tr>
<tr>
<td><b>564</b></td>
<td>New Hampshire Roller Derby</td>
<td>New Hampshire</td>
<td>Womens</td>
<td>.43808</td>
</tr>
<tr>
<td><b>565</b></td>
<td>Bellingham FLASH</td>
<td>Bellingham</td>
<td>Womens</td>
<td>.43743</td>
</tr>
<tr>
<td><b>566</b></td>
<td>Roller Derby Twente</td>
<td>Twente</td>
<td>Womens</td>
<td>.43734</td>
</tr>
<tr>
<td><b>567</b></td>
<td>Northwest Derby Company</td>
<td>Northwest</td>
<td>Womens</td>
<td>.43651</td>
</tr>
<tr>
<td><b>568</b></td>
<td>Kingston City Rollers</td>
<td>Kingston City</td>
<td>Womens</td>
<td>.43631</td>
</tr>
<tr>
<td><b>569</b></td>
<td>Fight Hawks</td>
<td>Granite City</td>
<td>Womens</td>
<td>.43606</td>
</tr>
<tr>
<td><b>570</b></td>
<td>The Anguanas Roller Derby Vicenza</td>
<td>Anguanas</td>
<td>Womens</td>
<td>.43571</td>
</tr>
<tr>
<td><b>571</b></td>
<td>Big Sky All Stars</td>
<td>Big Sky</td>
<td>Womens</td>
<td>.43491</td>
</tr>
<tr>
<td><b>572</b></td>
<td>Bembel Town Rollergirls</td>
<td>Bembeltown</td>
<td>Womens</td>
<td>.43438</td>
</tr>
<tr>
<td><b>573</b></td>
<td>Nottingham Roller Girls</td>
<td>Nottingham</td>
<td>Womens</td>
<td>.43424</td>
</tr>
<tr>
<td><b>574</b></td>
<td>Barockcity Rollerderby</td>
<td>Barockcity</td>
<td>Womens</td>
<td>.43424</td>
</tr>
<tr>
<td><b>575</b></td>
<td>Aarhus Derby Danes</td>
<td>Aarhus</td>
<td>Womens</td>
<td>.43314</td>
</tr>
<tr>
<td><b>576</b></td>
<td>Subzero Sirens</td>
<td>Queen City</td>
<td>Womens</td>
<td>.43236</td>
</tr>
<tr>
<td><b>577</b></td>
<td>Lyon Association Roller Derby</td>
<td>Lyonnaises</td>
<td>Womens</td>
<td>.43222</td>
</tr>
<tr>
<td><b>578</b></td>
<td>Reading Derby Girls</td>
<td>Reading</td>
<td>Womens</td>
<td>.43195</td>
</tr>
<tr>
<td><b>579</b></td>
<td>New Jersey Roller Derby</td>
<td>Morristown: NJRD</td>
<td>Womens</td>
<td>.43162</td>
</tr>
<tr>
<td><b>580</b></td>
<td>Savannah Derby Devils</td>
<td>Savannah</td>
<td>Womens</td>
<td>.43129</td>
</tr>
<tr>
<td><b>581</b></td>
<td>Coachella Valley Derby Girls</td>
<td>Coachella Valley</td>
<td>Womens</td>
<td>.43110</td>
</tr>
<tr>
<td><b>582</b></td>
<td>Ring City Rollergirls</td>
<td>Ring City</td>
<td>Womens</td>
<td>.43105</td>
</tr>
<tr>
<td><b>583</b></td>
<td>Hellions of Troy Roller Derby</td>
<td>Hellions</td>
<td>Womens</td>
<td>.43041</td>
</tr>
<tr>
<td><b>584</b></td>
<td>Roller Derby Belfort</td>
<td>Belfort</td>
<td>Womens</td>
<td>.43038</td>
</tr>
<tr>
<td><b>585</b></td>
<td>580 Rollergirls</td>
<td>580</td>
<td>Womens</td>
<td>.43037</td>
</tr>
<tr>
<td><b>586</b></td>
<td>El Paso Roller Derby</td>
<td>El Paso</td>
<td>Womens</td>
<td>.43028</td>
</tr>
<tr>
<td><b>587</b></td>
<td>Killah Beez</td>
<td>Providence</td>
<td>Womens</td>
<td>.42959</td>
</tr>
<tr>
<td><b>588</b></td>
<td>Audio Assault</td>
<td>NEO</td>
<td>Womens</td>
<td>.42940</td>
</tr>
<tr>
<td><b>589</b></td>
<td>The Parliament of Pain</td>
<td>The Parliament of Pain</td>
<td>Womens</td>
<td>.42938</td>
</tr>
<tr>
<td><b>590</b></td>
<td>Hazmat Crew</td>
<td>Burning River</td>
<td>Womens</td>
<td>.42904</td>
</tr>
<tr>
<td><b>591</b></td>
<td>Club Roller Derby 38</td>
<td>Marmots</td>
<td>Womens</td>
<td>.42868</td>
</tr>
<tr>
<td><b>592</b></td>
<td>Valkyrias Roller Derby</td>
<td>Valkyrias</td>
<td>Womens</td>
<td>.42861</td>
</tr>
<tr>
<td><b>593</b></td>
<td>Project Mayhem</td>
<td>Rocky Mtn.</td>
<td>Womens</td>
<td>.42855</td>
</tr>
<tr>
<td><b>594</b></td>
<td>Bangor Roller Derby B-Team</td>
<td>Bangor</td>
<td>Womens</td>
<td>.42839</td>
</tr>
<tr>
<td><b>595</b></td>
<td>Wreckin' Roller Rebels</td>
<td>Wreckin' Rebels</td>
<td>Womens</td>
<td>.42828</td>
</tr>
<tr>
<td><b>596</b></td>
<td>Västerås Roller Derby</td>
<td>Västerås</td>
<td>Womens</td>
<td>.42803</td>
</tr>
<tr>
<td><b>597</b></td>
<td>Mad Hitters</td>
<td>Muddy River</td>
<td>Womens</td>
<td>.42791</td>
</tr>
<tr>
<td><b>598</b></td>
<td>Echo City Knockouts</td>
<td>Echo City</td>
<td>Womens</td>
<td>.42787</td>
</tr>
<tr>
<td><b>599</b></td>
<td>Black Harrts</td>
<td>Cape Fear</td>
<td>Womens</td>
<td>.42756</td>
</tr>
<tr>
<td><b>600</b></td>
<td>Diamond Valley Roller Derby Club</td>
<td>Diamond Valley</td>
<td>Womens</td>
<td>.42699</td>
</tr>
<tr>
<td><b>601</b></td>
<td>The Cubs</td>
<td>Gent Go Go</td>
<td>Womens</td>
<td>.42690</td>
</tr>
<tr>
<td><b>602</b></td>
<td>West Coast Derby Knockouts</td>
<td>West Coast Knockouts</td>
<td>Womens</td>
<td>.42610</td>
</tr>
<tr>
<td><b>603</b></td>
<td>Brick House Betties</td>
<td>Brick House Betties</td>
<td>Womens</td>
<td>.42606</td>
</tr>
<tr>
<td><b>604</b></td>
<td>Fierce Valley Roller Girls</td>
<td>Fierce Valley</td>
<td>Womens</td>
<td>.42601</td>
</tr>
<tr>
<td><b>605</b></td>
<td>Devil Dog Derby Dames</td>
<td>Devil Dog Derby</td>
<td>Womens</td>
<td>.42598</td>
</tr>
<tr>
<td><b>606</b></td>
<td>SWAT team</td>
<td>Ft. Wayne</td>
<td>Womens</td>
<td>.42589</td>
</tr>
<tr>
<td><b>607</b></td>
<td>Boom Town Derby Dames</td>
<td>Boom Town</td>
<td>Womens</td>
<td>.42576</td>
</tr>
<tr>
<td><b>608</b></td>
<td>Juggernaughties</td>
<td>Duke</td>
<td>Womens</td>
<td>.42556</td>
</tr>
<tr>
<td><b>609</b></td>
<td>Lightning</td>
<td>Paradise City</td>
<td>Womens</td>
<td>.42524</td>
</tr>
<tr>
<td><b>610</b></td>
<td>Westside Wreck Hers Roller Derby</td>
<td>Wreck Hers</td>
<td>Womens</td>
<td>.42471</td>
</tr>
<tr>
<td><b>611</b></td>
<td>Ballarat Roller Derby League</td>
<td>Ballarat</td>
<td>Womens</td>
<td>.42463</td>
</tr>
<tr>
<td><b>612</b></td>
<td>Harrisburg Area Roller Derby</td>
<td>Harrisburg</td>
<td>Womens</td>
<td>.42411</td>
</tr>
<tr>
<td><b>613</b></td>
<td>Black-n-Bluegrass RollerGirls</td>
<td>Black-n-Bluegrass</td>
<td>Womens</td>
<td>.42364</td>
</tr>
<tr>
<td><b>614</b></td>
<td>Maiden Grrders</td>
<td>Glasgow</td>
<td>Womens</td>
<td>.42275</td>
</tr>
<tr>
<td><b>615</b></td>
<td>BisMan Roller Derby (Women's)</td>
<td>Bombshellz</td>
<td>Womens</td>
<td>.42233</td>
</tr>
<tr>
<td><b>616</b></td>
<td>Hidden City Derby Girls</td>
<td>Hidden City</td>
<td>Womens</td>
<td>.42213</td>
</tr>
<tr>
<td><b>617</b></td>
<td>Glorious Batardes</td>
<td>Lille</td>
<td>Womens</td>
<td>.42174</td>
</tr>
<tr>
<td><b>618</b></td>
<td>Fargo Moorhead Derby Girls</td>
<td>Fargo Moorhead</td>
<td>Womens</td>
<td>.42164</td>
</tr>
<tr>
<td><b>619</b></td>
<td>South West Sask Roller Derby Association</td>
<td>Redneck Betties</td>
<td>Womens</td>
<td>.42153</td>
</tr>
<tr>
<td><b>620</b></td>
<td>Thunder City Derby Sirens</td>
<td>Thunder City</td>
<td>Womens</td>
<td>.42140</td>
</tr>
<tr>
<td><b>621</b></td>
<td>Carson Victory Rollers</td>
<td>Carson</td>
<td>Womens</td>
<td>.42128</td>
</tr>
<tr>
<td><b>622</b></td>
<td>Ohio Valley Roller Girls</td>
<td>Ohio Valley</td>
<td>Womens</td>
<td>.42116</td>
</tr>
<tr>
<td><b>623</b></td>
<td>Two Rivers Roller Derby</td>
<td>Two Rivers</td>
<td>Womens</td>
<td>.42094</td>
</tr>
<tr>
<td><b>624</b></td>
<td>Bay City Rollers</td>
<td>Bay City</td>
<td>Womens</td>
<td>.42076</td>
</tr>
<tr>
<td><b>625</b></td>
<td>Outlaws Roller Derby</td>
<td>Outlaws Roller Derby</td>
<td>Womens</td>
<td>.42055</td>
</tr>
<tr>
<td><b>626</b></td>
<td>Milton Keynes Roller Derby</td>
<td>Milton Keynes</td>
<td>Womens</td>
<td>.42030</td>
</tr>
<tr>
<td><b>627</b></td>
<td>Thunder Bay Roller Derby</td>
<td>Thunder Bay</td>
<td>Womens</td>
<td>.42021</td>
</tr>
<tr>
<td><b>628</b></td>
<td>Breakwater Blackhearts</td>
<td>Rock Coast</td>
<td>Womens</td>
<td>.41958</td>
</tr>
<tr>
<td><b>629</b></td>
<td>East Side Wheelers</td>
<td>East Side Wheelers</td>
<td>Womens</td>
<td>.41932</td>
</tr>
<tr>
<td><b>630</b></td>
<td>Belmont Bruisers</td>
<td>Charlottesville</td>
<td>Womens</td>
<td>.41895</td>
</tr>
<tr>
<td><b>631</b></td>
<td>Circle City Derby Girls</td>
<td>Circle City</td>
<td>Womens</td>
<td>.41891</td>
</tr>
<tr>
<td><b>632</b></td>
<td>Twisted Sisters (BCR)</td>
<td>Bay City</td>
<td>Womens</td>
<td>.41806</td>
</tr>
<tr>
<td><b>633</b></td>
<td>Soul City Sirens</td>
<td>Soul City</td>
<td>Womens</td>
<td>.41786</td>
</tr>
<tr>
<td><b>634</b></td>
<td>Female Trouble</td>
<td>Charm City</td>
<td>Womens</td>
<td>.41714</td>
</tr>
<tr>
<td><b>635</b></td>
<td>Dakota City Demolition Crew</td>
<td>Dakota City</td>
<td>Womens</td>
<td>.41705</td>
</tr>
<tr>
<td><b>636</b></td>
<td>Toowoomba City Rollers</td>
<td>Toowoomba</td>
<td>Womens</td>
<td>.41684</td>
</tr>
<tr>
<td><b>637</b></td>
<td>Black Diamond Rollers</td>
<td>Black Diamond</td>
<td>Womens</td>
<td>.41646</td>
</tr>
<tr>
<td><b>638</b></td>
<td>Wonder Brawlers</td>
<td>Central NY</td>
<td>Womens</td>
<td>.41599</td>
</tr>
<tr>
<td><b>639</b></td>
<td>Central Arkansas Roller Derby</td>
<td>Central Arkansas</td>
<td>Womens</td>
<td>.41599</td>
</tr>
<tr>
<td><b>640</b></td>
<td>Bourbon Brawlers</td>
<td>Derby City</td>
<td>Womens</td>
<td>.41581</td>
</tr>
<tr>
<td><b>641</b></td>
<td>Piritorin Ässät</td>
<td>Kallio</td>
<td>Womens</td>
<td>.41538</td>
</tr>
<tr>
<td><b>642</b></td>
<td>Albany All Stars Roller Derby</td>
<td>Albany</td>
<td>Womens</td>
<td>.41527</td>
</tr>
<tr>
<td><b>643</b></td>
<td>Dam City Rollers</td>
<td>Dam City</td>
<td>Womens</td>
<td>.41454</td>
</tr>
<tr>
<td><b>644</b></td>
<td>Suffolk Roller Derby (Women's)</td>
<td>Suffolk (Women's)</td>
<td>Womens</td>
<td>.41452</td>
</tr>
<tr>
<td><b>645</b></td>
<td>Durham Region Roller Derby</td>
<td>Durham (Canada)</td>
<td>Womens</td>
<td>.41439</td>
</tr>
<tr>
<td><b>646</b></td>
<td>Flour City Fear Men's Roller Derby</td>
<td>Flour City</td>
<td>Mens</td>
<td>.41392</td>
</tr>
<tr>
<td><b>647</b></td>
<td>Beloit Bombshells</td>
<td>Beloit Bombshells</td>
<td>Womens</td>
<td>.41339</td>
</tr>
<tr>
<td><b>648</b></td>
<td>Wiltshire Roller Derby</td>
<td>Wiltshire</td>
<td>Womens</td>
<td>.41327</td>
</tr>
<tr>
<td><b>649</b></td>
<td>Battalion of Skates</td>
<td>Ventura</td>
<td>Womens</td>
<td>.41291</td>
</tr>
<tr>
<td><b>650</b></td>
<td>Black Ice Brawlers</td>
<td>Green Mt.</td>
<td>Womens</td>
<td>.41261</td>
</tr>
<tr>
<td><b>651</b></td>
<td>Flint Roller Derby</td>
<td>Flint City</td>
<td>Womens</td>
<td>.41245</td>
</tr>
<tr>
<td><b>652</b></td>
<td>Shade Brigade</td>
<td>Chicago Outfit</td>
<td>Womens</td>
<td>.41243</td>
</tr>
<tr>
<td><b>653</b></td>
<td>Tweed Valley Rollers</td>
<td>Tweed Valley</td>
<td>Womens</td>
<td>.41240</td>
</tr>
<tr>
<td><b>654</b></td>
<td>State College Area Roller Derby</td>
<td>State College</td>
<td>Womens</td>
<td>.41211</td>
</tr>
<tr>
<td><b>655</b></td>
<td>Miss B-havers</td>
<td>Columbia</td>
<td>Womens</td>
<td>.41161</td>
</tr>
<tr>
<td><b>656</b></td>
<td>Lil Chicago Roller Derby</td>
<td>Lil Chicago</td>
<td>Womens</td>
<td>.41150</td>
</tr>
<tr>
<td><b>657</b></td>
<td>Compagnie Cruelle</td>
<td>Bordeaux</td>
<td>Womens</td>
<td>.41144</td>
</tr>
<tr>
<td><b>658</b></td>
<td>Enchanted Mountain Roller Derby</td>
<td>Enchanted Mountain</td>
<td>Womens</td>
<td>.41142</td>
</tr>
<tr>
<td><b>659</b></td>
<td>Renegade Derby Dames</td>
<td>Renegade</td>
<td>Womens</td>
<td>.41130</td>
</tr>
<tr>
<td><b>660</b></td>
<td>Spokannibals</td>
<td>Spokannibals</td>
<td>Womens</td>
<td>.41038</td>
</tr>
<tr>
<td><b>661</b></td>
<td>Mount Militia Derby Crew</td>
<td>Mount Militia</td>
<td>Womens</td>
<td>.41016</td>
</tr>
<tr>
<td><b>662</b></td>
<td>Wellington Roller Derby</td>
<td>Feims</td>
<td>Womens</td>
<td>.40962</td>
</tr>
<tr>
<td><b>663</b></td>
<td>Orange Crush</td>
<td>Rage City</td>
<td>Womens</td>
<td>.40960</td>
</tr>
<tr>
<td><b>664</b></td>
<td>Capital Corruption</td>
<td>Lansing Vixens</td>
<td>Womens</td>
<td>.40940</td>
</tr>
<tr>
<td><b>665</b></td>
<td>Albany B Team</td>
<td>Albany</td>
<td>Womens</td>
<td>.40924</td>
</tr>
<tr>
<td><b>666</b></td>
<td>Salina Sirens Roller Derby</td>
<td>Salina Sirens</td>
<td>Womens</td>
<td>.40920</td>
</tr>
<tr>
<td><b>667</b></td>
<td>Rainbow Furies</td>
<td>Toulouse</td>
<td>Womens</td>
<td>.40901</td>
</tr>
<tr>
<td><b>668</b></td>
<td>C-Stars</td>
<td>Stockholm</td>
<td>Womens</td>
<td>.40891</td>
</tr>
<tr>
<td><b>669</b></td>
<td>Bristol Roller Derby B</td>
<td>Bristol A</td>
<td>Womens</td>
<td>.40814</td>
</tr>
<tr>
<td><b>670</b></td>
<td>Sis-Q Rollerz</td>
<td>Sis-Q</td>
<td>Womens</td>
<td>.40812</td>
</tr>
<tr>
<td><b>671</b></td>
<td>Northland Nightmares Roller Girlz</td>
<td>Northland Nightmares</td>
<td>Womens</td>
<td>.40779</td>
</tr>
<tr>
<td><b>672</b></td>
<td>Port Macquarie Roller Derby</td>
<td>Port Macquarie</td>
<td>Womens</td>
<td>.40732</td>
</tr>
<tr>
<td><b>673</b></td>
<td>Rayo Dockers Roller Derby</td>
<td>Rayo Dockers</td>
<td>Womens</td>
<td>.40691</td>
</tr>
<tr>
<td><b>674</b></td>
<td>Seaside Siren Roller Girls</td>
<td>Seaside Sirens</td>
<td>Womens</td>
<td>.40664</td>
</tr>
<tr>
<td><b>675</b></td>
<td>Brigade of Handsome Gentlemen</td>
<td>Handsome Gentlemen</td>
<td>Mens</td>
<td>.40651</td>
</tr>
<tr>
<td><b>676</b></td>
<td>Gainesville Roller Rebels</td>
<td>Gainesville</td>
<td>Womens</td>
<td>.40616</td>
</tr>
<tr>
<td><b>677</b></td>
<td>Jerzey Derby Brigade</td>
<td>Morristown: JDB</td>
<td>Womens</td>
<td>.40581</td>
</tr>
<tr>
<td><b>678</b></td>
<td>Sioux Falls Roller Dollz</td>
<td>Sioux Falls</td>
<td>Womens</td>
<td>.40562</td>
</tr>
<tr>
<td><b>679</b></td>
<td>Mississippi Valley Mayhem</td>
<td>Mississippi Valley</td>
<td>Womens</td>
<td>.40543</td>
</tr>
<tr>
<td><b>680</b></td>
<td>Orlando Psycho City Derby Girls</td>
<td>Psycho City</td>
<td>Womens</td>
<td>.40520</td>
</tr>
<tr>
<td><b>681</b></td>
<td>Nice Roller Derby</td>
<td>Nice</td>
<td>Womens</td>
<td>.40504</td>
</tr>
<tr>
<td><b>682</b></td>
<td>Motherlode Area Derby</td>
<td>MAD</td>
<td>Womens</td>
<td>.40437</td>
</tr>
<tr>
<td><b>683</b></td>
<td>Maui Rollergirls</td>
<td>Maui</td>
<td>Womens</td>
<td>.40420</td>
</tr>
<tr>
<td><b>684</b></td>
<td>Diamond District</td>
<td>Gotham</td>
<td>Womens</td>
<td>.40416</td>
</tr>
<tr>
<td><b>685</b></td>
<td>Glass City Rollers</td>
<td>Glass City</td>
<td>Womens</td>
<td>.40387</td>
</tr>
<tr>
<td><b>686</b></td>
<td>The B-Headers</td>
<td>Royal Windsor</td>
<td>Womens</td>
<td>.40383</td>
</tr>
<tr>
<td><b>687</b></td>
<td>Dead River Derby</td>
<td>Dead River</td>
<td>Womens</td>
<td>.40369</td>
</tr>
<tr>
<td><b>688</b></td>
<td>Dorset Roller Girls</td>
<td>Dorset</td>
<td>Womens</td>
<td>.40342</td>
</tr>
<tr>
<td><b>689</b></td>
<td>Tar Sand Betties</td>
<td>Tar Sand Betties</td>
<td>Womens</td>
<td>.40333</td>
</tr>
<tr>
<td><b>690</b></td>
<td>Badasses</td>
<td>Rockin' Rollers</td>
<td>Womens</td>
<td>.40287</td>
</tr>
<tr>
<td><b>691</b></td>
<td>Roller Underground</td>
<td>Roller Underground</td>
<td>Womens</td>
<td>.40283</td>
</tr>
<tr>
<td><b>692</b></td>
<td>Small Town Outlaws</td>
<td>Small Town</td>
<td>Womens</td>
<td>.40265</td>
</tr>
<tr>
<td><b>693</b></td>
<td>Grapes of Wrath</td>
<td>Wine Town</td>
<td>Womens</td>
<td>.40258</td>
</tr>
<tr>
<td><b>694</b></td>
<td>Central Coast Roller Derby United</td>
<td>Central Coast (NSW)</td>
<td>Womens</td>
<td>.40184</td>
</tr>
<tr>
<td><b>695</b></td>
<td>Brawlin' Broads</td>
<td>Bay State Brawlers</td>
<td>Womens</td>
<td>.40153</td>
</tr>
<tr>
<td><b>696</b></td>
<td>Kalamazoo Men's Roller Derby</td>
<td>Kalamazoo Men's</td>
<td>Mens</td>
<td>.40115</td>
</tr>
<tr>
<td><b>697</b></td>
<td>Roma Roller Derby</td>
<td>Roma</td>
<td>Womens</td>
<td>.40046</td>
</tr>
<tr>
<td><b>698</b></td>
<td>Mason-Dixon Roller Vixens</td>
<td>Mason-Dixon</td>
<td>Womens</td>
<td>.40012</td>
</tr>
<tr>
<td><b>699</b></td>
<td>Loco City Derby Girls</td>
<td>Loco City</td>
<td>Womens</td>
<td>.40007</td>
</tr>
<tr>
<td><b>700</b></td>
<td>Bootleg City Roller Derby</td>
<td>Moonshine Maidens</td>
<td>Womens</td>
<td>.40006</td>
</tr>
<tr>
<td><b>701</b></td>
<td>Destruction Dames</td>
<td>Demolition</td>
<td>Womens</td>
<td>.39980</td>
</tr>
<tr>
<td><b>702</b></td>
<td>West Texas Roller Dollz</td>
<td>West Texas</td>
<td>Womens</td>
<td>.39977</td>
</tr>
<tr>
<td><b>703</b></td>
<td>Preston Roller Girls</td>
<td>Preston</td>
<td>Womens</td>
<td>.39952</td>
</tr>
<tr>
<td><b>704</b></td>
<td>Hell's Belles</td>
<td>St. Chux</td>
<td>Womens</td>
<td>.39916</td>
</tr>
<tr>
<td><b>705</b></td>
<td>North Cs</td>
<td>Newcastle</td>
<td>Womens</td>
<td>.39819</td>
</tr>
<tr>
<td><b>706</b></td>
<td>Ume Radical Rollers</td>
<td>Ume</td>
<td>Womens</td>
<td>.39718</td>
</tr>
<tr>
<td><b>707</b></td>
<td>Cat 5’s</td>
<td>Gold Coast (FL)</td>
<td>Womens</td>
<td>.39717</td>
</tr>
<tr>
<td><b>708</b></td>
<td>Superior Sirens</td>
<td>Dead River</td>
<td>Womens</td>
<td>.39688</td>
</tr>
<tr>
<td><b>709</b></td>
<td>Men's Roller Derby of Kentucky</td>
<td>Kentucky Men's</td>
<td>Mens</td>
<td>.39684</td>
</tr>
<tr>
<td><b>710</b></td>
<td>Roller Derby Alcoy</td>
<td>Alcoy</td>
<td>Womens</td>
<td>.39659</td>
</tr>
<tr>
<td><b>711</b></td>
<td>Sirens</td>
<td>Rideau Valley</td>
<td>Womens</td>
<td>.39654</td>
</tr>
<tr>
<td><b>712</b></td>
<td>French Broads</td>
<td>Blue Ridge</td>
<td>Womens</td>
<td>.39628</td>
</tr>
<tr>
<td><b>713</b></td>
<td>Bath City Roller Girls</td>
<td>Bath City</td>
<td>Womens</td>
<td>.39616</td>
</tr>
<tr>
<td><b>714</b></td>
<td>Kindersley Roller Derby Association</td>
<td>Crude Hitters</td>
<td>Womens</td>
<td>.39596</td>
</tr>
<tr>
<td><b>715</b></td>
<td>The Flaming Noras</td>
<td>Furness Women's</td>
<td>Womens</td>
<td>.39593</td>
</tr>
<tr>
<td><b>716</b></td>
<td>Kouvola Rock n Rollers B</td>
<td>Kouvola</td>
<td>Womens</td>
<td>.39499</td>
</tr>
<tr>
<td><b>717</b></td>
<td>Rainy City Roller Dolls</td>
<td>Rainy City (WA)</td>
<td>Womens</td>
<td>.39497</td>
</tr>
<tr>
<td><b>718</b></td>
<td>Aroostook Roller Derby</td>
<td>Aroostook</td>
<td>Womens</td>
<td>.39416</td>
</tr>
<tr>
<td><b>719</b></td>
<td>Roller Derby Tournai</td>
<td>Tournai</td>
<td>Womens</td>
<td>.39404</td>
</tr>
<tr>
<td><b>720</b></td>
<td>Crimson Vipers (Roller Derby Bergamo)</td>
<td>Bergamo</td>
<td>Womens</td>
<td>.39400</td>
</tr>
<tr>
<td><b>721</b></td>
<td>Spring Blocks</td>
<td>All Blocks</td>
<td>Womens</td>
<td>.39395</td>
</tr>
<tr>
<td><b>722</b></td>
<td>Pulp Affliction</td>
<td>ORG All-Stars</td>
<td>Womens</td>
<td>.39353</td>
</tr>
<tr>
<td><b>723</b></td>
<td>Free State Roller Derby</td>
<td>Free State</td>
<td>Womens</td>
<td>.39344</td>
</tr>
<tr>
<td><b>724</b></td>
<td>Magnolia Roller Vixens</td>
<td>Magnolia Roller Vixens</td>
<td>Womens</td>
<td>.39334</td>
</tr>
<tr>
<td><b>725</b></td>
<td>Weyburn Roller Derby Association</td>
<td>Weyburn</td>
<td>Womens</td>
<td>.39312</td>
</tr>
<tr>
<td><b>726</b></td>
<td>Roller Derby Rouen</td>
<td>Rouen</td>
<td>Womens</td>
<td>.39311</td>
</tr>
<tr>
<td><b>727</b></td>
<td>Cen-Tex Roller Girls</td>
<td>Cen-Tex</td>
<td>Womens</td>
<td>.39307</td>
</tr>
<tr>
<td><b>728</b></td>
<td>Durango Roller Girls</td>
<td>Durango</td>
<td>Womens</td>
<td>.39290</td>
</tr>
<tr>
<td><b>729</b></td>
<td>Whidbey Island Roller Girls</td>
<td>Whidbey Island</td>
<td>Womens</td>
<td>.39278</td>
</tr>
<tr>
<td><b>730</b></td>
<td>Roller Derby Pibrac</td>
<td>Pibrac</td>
<td>Womens</td>
<td>.39277</td>
</tr>
<tr>
<td><b>731</b></td>
<td>Columbia Basin Roller Derby</td>
<td>Columbia Basin</td>
<td>Womens</td>
<td>.39213</td>
</tr>
<tr>
<td><b>732</b></td>
<td>Paradise Roller Girls</td>
<td>Paradise Roller Girls</td>
<td>Womens</td>
<td>.39198</td>
</tr>
<tr>
<td><b>733</b></td>
<td>Mid State Sisters of Skate</td>
<td>Mid-State</td>
<td>Womens</td>
<td>.39156</td>
</tr>
<tr>
<td><b>734</b></td>
<td>South Shore Roller Girls</td>
<td>South Shore</td>
<td>Womens</td>
<td>.39155</td>
</tr>
<tr>
<td><b>735</b></td>
<td>Killa Hurtz Roller Girls</td>
<td>Killa Hurtz</td>
<td>Womens</td>
<td>.39155</td>
</tr>
<tr>
<td><b>736</b></td>
<td>Border City Brawlers</td>
<td>Border City Brawlers</td>
<td>Womens</td>
<td>.39153</td>
</tr>
<tr>
<td><b>737</b></td>
<td>Light City Derby (Womens)</td>
<td>Light City</td>
<td>Womens</td>
<td>.39104</td>
</tr>
<tr>
<td><b>738</b></td>
<td>Dublin Roller Derby C</td>
<td>Dublin</td>
<td>Womens</td>
<td>.39099</td>
</tr>
<tr>
<td><b>739</b></td>
<td>Block Party</td>
<td>Philly</td>
<td>Womens</td>
<td>.39018</td>
</tr>
<tr>
<td><b>740</b></td>
<td>Rockford Rage Roller Derby</td>
<td>Rockford</td>
<td>Womens</td>
<td>.38993</td>
</tr>
<tr>
<td><b>741</b></td>
<td>MedCity Mafia Roller Derby</td>
<td>Med City</td>
<td>Womens</td>
<td>.38987</td>
</tr>
<tr>
<td><b>742</b></td>
<td>Traverse City Roller Derby</td>
<td>Traverse City</td>
<td>Womens</td>
<td>.38953</td>
</tr>
<tr>
<td><b>743</b></td>
<td>Spartanburg Deadly Dolls</td>
<td>Deadly Dolls</td>
<td>Womens</td>
<td>.38914</td>
</tr>
<tr>
<td><b>744</b></td>
<td>Yellow Rose Derby Girls</td>
<td>Yellow Rose</td>
<td>Womens</td>
<td>.38830</td>
</tr>
<tr>
<td><b>745</b></td>
<td>Marietta</td>
<td>Peach State</td>
<td>Womens</td>
<td>.38808</td>
</tr>
<tr>
<td><b>746</b></td>
<td>Lethbridge Roller Derby Guild</td>
<td>Lethbridge</td>
<td>Womens</td>
<td>.38786</td>
</tr>
<tr>
<td><b>747</b></td>
<td>Surrey Roller Girls</td>
<td>Surrey (Women's)</td>
<td>Womens</td>
<td>.38775</td>
</tr>
<tr>
<td><b>748</b></td>
<td>Brawlers</td>
<td>Brandywine</td>
<td>Womens</td>
<td>.38760</td>
</tr>
<tr>
<td><b>749</b></td>
<td>Cenla Derby Dames</td>
<td>Cenla</td>
<td>Womens</td>
<td>.38674</td>
</tr>
<tr>
<td><b>750</b></td>
<td>G-Rap Attack!</td>
<td>Grand Raggidy</td>
<td>Womens</td>
<td>.38660</td>
</tr>
<tr>
<td><b>751</b></td>
<td>Kingston Derby Girls</td>
<td>Kingston</td>
<td>Womens</td>
<td>.38643</td>
</tr>
<tr>
<td><b>752</b></td>
<td>Flathead Valley Roller Derby</td>
<td>Flathead Valley</td>
<td>Womens</td>
<td>.38619</td>
</tr>
<tr>
<td><b>753</b></td>
<td>Wollongong Illawarra Roller Derby</td>
<td>Steel City Derby Dolls</td>
<td>Womens</td>
<td>.38615</td>
</tr>
<tr>
<td><b>754</b></td>
<td>Bruisin' Betties</td>
<td>Lowcountry</td>
<td>Womens</td>
<td>.38607</td>
</tr>
<tr>
<td><b>755</b></td>
<td>Wolverhampton Honour Rollers</td>
<td>Wolverhampton</td>
<td>Womens</td>
<td>.38599</td>
</tr>
<tr>
<td><b>756</b></td>
<td>Spitfires</td>
<td>Capital City</td>
<td>Womens</td>
<td>.38535</td>
</tr>
<tr>
<td><b>757</b></td>
<td>Cork City Firebirds</td>
<td>Cork City</td>
<td>Womens</td>
<td>.38524</td>
</tr>
<tr>
<td><b>758</b></td>
<td>Okanagan Derby Dolls</td>
<td>Okanagan Dolls</td>
<td>Womens</td>
<td>.38488</td>
</tr>
<tr>
<td><b>759</b></td>
<td>Perpignan Roller Derby</td>
<td>Perpignan</td>
<td>Womens</td>
<td>.38461</td>
</tr>
<tr>
<td><b>760</b></td>
<td>B Railers</td>
<td>Chattanooga</td>
<td>Womens</td>
<td>.38442</td>
</tr>
<tr>
<td><b>761</b></td>
<td>Rhein-Neckar Delta Quads</td>
<td>Delta Quads</td>
<td>Womens</td>
<td>.38439</td>
</tr>
<tr>
<td><b>762</b></td>
<td>Pensacola Roller Gurlz</td>
<td>Pensacola</td>
<td>Womens</td>
<td>.38436</td>
</tr>
<tr>
<td><b>763</b></td>
<td>Hel'z Belles Roller Derby</td>
<td>Hel'z Belles</td>
<td>Womens</td>
<td>.38406</td>
</tr>
<tr>
<td><b>764</b></td>
<td>Derby Roller Provence Méditerranée</td>
<td>Provence Méditerranée</td>
<td>Womens</td>
<td>.38403</td>
</tr>
<tr>
<td><b>765</b></td>
<td>Girls Rollin in the South</td>
<td>GRITS</td>
<td>Womens</td>
<td>.38367</td>
</tr>
<tr>
<td><b>766</b></td>
<td>SWAT B Team</td>
<td>Angels of Terror</td>
<td>Womens</td>
<td>.38365</td>
</tr>
<tr>
<td><b>767</b></td>
<td>Prince Albert Roller Derby</td>
<td>Outlaws</td>
<td>Womens</td>
<td>.38323</td>
</tr>
<tr>
<td><b>768</b></td>
<td>Aurora 88s Roller Derby</td>
<td>Aurora 88s</td>
<td>Womens</td>
<td>.38304</td>
</tr>
<tr>
<td><b>769</b></td>
<td>Roller Derby Pays d'Aix (Womens)</td>
<td>Pays d'Aix Womens</td>
<td>Womens</td>
<td>.38262</td>
</tr>
<tr>
<td><b>770</b></td>
<td>Nuclear Free Roller Derby League</td>
<td>Nuclear Free</td>
<td>Womens</td>
<td>.38219</td>
</tr>
<tr>
<td><b>771</b></td>
<td>Battery Brigade</td>
<td>Assault City</td>
<td>Womens</td>
<td>.38199</td>
</tr>
<tr>
<td><b>772</b></td>
<td>Twin City Knockers</td>
<td>Knockers</td>
<td>Womens</td>
<td>.38189</td>
</tr>
<tr>
<td><b>773</b></td>
<td>Floral City Roller Girls</td>
<td>Floral City</td>
<td>Womens</td>
<td>.38179</td>
</tr>
<tr>
<td><b>774</b></td>
<td>Mansfield Roller Derby B team</td>
<td>Mansfield</td>
<td>Womens</td>
<td>.38141</td>
</tr>
<tr>
<td><b>775</b></td>
<td>Les Bûches</td>
<td>Bûches</td>
<td>Womens</td>
<td>.38127</td>
</tr>
<tr>
<td><b>776</b></td>
<td>Joensuu Roller Derby</td>
<td>Joensuu</td>
<td>Womens</td>
<td>.38127</td>
</tr>
<tr>
<td><b>777</b></td>
<td>Forx Roller Derby</td>
<td>Forx Roller Derby</td>
<td>Womens</td>
<td>.38082</td>
</tr>
<tr>
<td><b>778</b></td>
<td>Lincolnshire Bombers</td>
<td>Lincolnshire</td>
<td>Womens</td>
<td>.38075</td>
</tr>
<tr>
<td><b>779</b></td>
<td>Durham Roller Derby</td>
<td>Durham</td>
<td>Womens</td>
<td>.38036</td>
</tr>
<tr>
<td><b>780</b></td>
<td>Piedmont Riot Roller Derby</td>
<td>Piedmont Riot</td>
<td>Womens</td>
<td>.37993</td>
</tr>
<tr>
<td><b>781</b></td>
<td>Fredericksburg Roller Derby</td>
<td>Fredericksburg</td>
<td>Womens</td>
<td>.37990</td>
</tr>
<tr>
<td><b>782</b></td>
<td>B-Sides</td>
<td>Roc City</td>
<td>Womens</td>
<td>.37963</td>
</tr>
<tr>
<td><b>783</b></td>
<td>South Florida Roller Girls</td>
<td>South Florida</td>
<td>Womens</td>
<td>.37920</td>
</tr>
<tr>
<td><b>784</b></td>
<td>The Militia</td>
<td>Dub City</td>
<td>Womens</td>
<td>.37909</td>
</tr>
<tr>
<td><b>785</b></td>
<td>Vendetta Vixens</td>
<td>Vendetta</td>
<td>Womens</td>
<td>.37889</td>
</tr>
<tr>
<td><b>786</b></td>
<td>Bad News Bs</td>
<td>Classic City</td>
<td>Womens</td>
<td>.37877</td>
</tr>
<tr>
<td><b>787</b></td>
<td>Central Maine Derby</td>
<td>Central Maine</td>
<td>Womens</td>
<td>.37841</td>
</tr>
<tr>
<td><b>788</b></td>
<td>Bath Roller Derby Girls</td>
<td>Bath Spartans</td>
<td>Womens</td>
<td>.37823</td>
</tr>
<tr>
<td><b>789</b></td>
<td>Susquehanna Valley Derby Vixens</td>
<td>Susquehanna Valley</td>
<td>Womens</td>
<td>.37807</td>
</tr>
<tr>
<td><b>790</b></td>
<td>Walla Walla Sweets Roller Girls</td>
<td>Walla Walla</td>
<td>Womens</td>
<td>.37803</td>
</tr>
<tr>
<td><b>791</b></td>
<td>Badlands Hellraisers Roller Derby</td>
<td>Hellraisers</td>
<td>Womens</td>
<td>.37762</td>
</tr>
<tr>
<td><b>792</b></td>
<td>Killa' Bees</td>
<td>Saskatoon</td>
<td>Womens</td>
<td>.37692</td>
</tr>
<tr>
<td><b>793</b></td>
<td>Battle Creek Cereal Killers</td>
<td>Battle Creek</td>
<td>Womens</td>
<td>.37690</td>
</tr>
<tr>
<td><b>794</b></td>
<td>Highland Derby Dolls</td>
<td>Highland Derby</td>
<td>Womens</td>
<td>.37679</td>
</tr>
<tr>
<td><b>795</b></td>
<td>Grin 'N' Barum Derby Girls</td>
<td>Grin 'N' Barum</td>
<td>Womens</td>
<td>.37671</td>
</tr>
<tr>
<td><b>796</b></td>
<td>Apple City Roller Derby</td>
<td>Apple City</td>
<td>Womens</td>
<td>.37643</td>
</tr>
<tr>
<td><b>797</b></td>
<td>Athens Ohio Roller Derby</td>
<td>Hell Betties</td>
<td>Womens</td>
<td>.37630</td>
</tr>
<tr>
<td><b>798</b></td>
<td>South Side Derby Dames</td>
<td>South Side (CO)</td>
<td>Womens</td>
<td>.37611</td>
</tr>
<tr>
<td><b>799</b></td>
<td>Electric City Roller GrrrlZ</td>
<td>Electric City</td>
<td>Womens</td>
<td>.37570</td>
</tr>
<tr>
<td><b>800</b></td>
<td>Platte Valley Roller Vixens</td>
<td>Platte Valley</td>
<td>Womens</td>
<td>.37556</td>
</tr>
<tr>
<td><b>801</b></td>
<td>Central Kansas Roller Girls</td>
<td>Central Kansas</td>
<td>Womens</td>
<td>.37480</td>
</tr>
<tr>
<td><b>802</b></td>
<td>Broadside Brawlers</td>
<td>Pirate City</td>
<td>Womens</td>
<td>.37462</td>
</tr>
<tr>
<td><b>803</b></td>
<td>Yankee Brutals</td>
<td>Connecticut</td>
<td>Womens</td>
<td>.37451</td>
</tr>
<tr>
<td><b>804</b></td>
<td>Red River Roller Derby</td>
<td>Red River</td>
<td>Womens</td>
<td>.37427</td>
</tr>
<tr>
<td><b>805</b></td>
<td>Code Blue Assassins</td>
<td>Bleeding Heartland</td>
<td>Womens</td>
<td>.37399</td>
</tr>
<tr>
<td><b>806</b></td>
<td>Dragon City Derby Dolls</td>
<td>Chikos</td>
<td>Womens</td>
<td>.37379</td>
</tr>
<tr>
<td><b>807</b></td>
<td>Hwy 14 Derby Association</td>
<td>Hwy 14</td>
<td>Womens</td>
<td>.37318</td>
</tr>
<tr>
<td><b>808</b></td>
<td>Quabbin Missile Crisis</td>
<td>Western Mass Destruction</td>
<td>Womens</td>
<td>.37317</td>
</tr>
<tr>
<td><b>809</b></td>
<td>Lyon Roller Derby (Womens)</td>
<td>Lyon</td>
<td>Womens</td>
<td>.37317</td>
</tr>
<tr>
<td><b>810</b></td>
<td>Wilkes-Barre/Scranton Roller Radicals</td>
<td>Roller Radicals</td>
<td>Womens</td>
<td>.37311</td>
</tr>
<tr>
<td><b>811</b></td>
<td>North Cheshire Victory Rollers</td>
<td>North Cheshire</td>
<td>Womens</td>
<td>.37292</td>
</tr>
<tr>
<td><b>812</b></td>
<td>Rogue Scholars</td>
<td>Varsity</td>
<td>Womens</td>
<td>.37279</td>
</tr>
<tr>
<td><b>813</b></td>
<td>Central West Roller Derby</td>
<td>CWA</td>
<td>Womens</td>
<td>.37267</td>
</tr>
<tr>
<td><b>814</b></td>
<td>Roller Derby Nîmes</td>
<td>Nîmes</td>
<td>Womens</td>
<td>.37252</td>
</tr>
<tr>
<td><b>815</b></td>
<td>Crime City C team</td>
<td>Crime City</td>
<td>Womens</td>
<td>.37251</td>
</tr>
<tr>
<td><b>816</b></td>
<td>Rumble Bees</td>
<td>Perth</td>
<td>Womens</td>
<td>.37240</td>
</tr>
<tr>
<td><b>817</b></td>
<td>Mean City Roller Derby (Women's)</td>
<td>Mean City Women</td>
<td>Womens</td>
<td>.37200</td>
</tr>
<tr>
<td><b>818</b></td>
<td>Cedar Rapids Rollergirls</td>
<td>Cedar Rapids Rollergirls</td>
<td>Womens</td>
<td>.37169</td>
</tr>
<tr>
<td><b>819</b></td>
<td>WestSide Derby Dollz (Women's)</td>
<td>WestSide (Women's)</td>
<td>Womens</td>
<td>.37146</td>
</tr>
<tr>
<td><b>820</b></td>
<td>Ocala Cannibals Roller Derby</td>
<td>Cannibals</td>
<td>Womens</td>
<td>.37138</td>
</tr>
<tr>
<td><b>821</b></td>
<td>Rock Villains</td>
<td>Free State</td>
<td>Womens</td>
<td>.37113</td>
</tr>
<tr>
<td><b>822</b></td>
<td>Boone Shiners</td>
<td>Appalachian Rollergirls</td>
<td>Womens</td>
<td>.37105</td>
</tr>
<tr>
<td><b>823</b></td>
<td>Morgantown Roller Vixens</td>
<td>Morgantown</td>
<td>Womens</td>
<td>.37087</td>
</tr>
<tr>
<td><b>824</b></td>
<td>Lafayette Brawlin' Dolls</td>
<td>Brawlin Dolls</td>
<td>Womens</td>
<td>.37009</td>
</tr>
<tr>
<td><b>825</b></td>
<td>Sans Culottes</td>
<td>Paris</td>
<td>Womens</td>
<td>.36972</td>
</tr>
<tr>
<td><b>826</b></td>
<td>Smoky Mountain Roller Girls</td>
<td>Smoky Mountain</td>
<td>Womens</td>
<td>.36970</td>
</tr>
<tr>
<td><b>827</b></td>
<td>Brighton Rockerbillies</td>
<td>Brighton (UK)</td>
<td>Womens</td>
<td>.36947</td>
</tr>
<tr>
<td><b>828</b></td>
<td>Monadnock Roller Derby</td>
<td>Monadnock</td>
<td>Womens</td>
<td>.36917</td>
</tr>
<tr>
<td><b>829</b></td>
<td>Chippewa Valley Roller Girls</td>
<td>Chippewa Valley</td>
<td>Womens</td>
<td>.36829</td>
</tr>
<tr>
<td><b>830</b></td>
<td>The Regulators</td>
<td>Gas City</td>
<td>Womens</td>
<td>.36816</td>
</tr>
<tr>
<td><b>831</b></td>
<td>Mouse River Rollers</td>
<td>Nodak Knockouts</td>
<td>Womens</td>
<td>.36808</td>
</tr>
<tr>
<td><b>832</b></td>
<td>Gladstone Roller Derby</td>
<td>Gladstone</td>
<td>Womens</td>
<td>.36772</td>
</tr>
<tr>
<td><b>833</b></td>
<td>Fairbanks Rollergirls</td>
<td>Fairbanks</td>
<td>Womens</td>
<td>.36645</td>
</tr>
<tr>
<td><b>834</b></td>
<td>Santas</td>
<td>Crossroads City</td>
<td>Womens</td>
<td>.36623</td>
</tr>
<tr>
<td><b>835</b></td>
<td>Åbo B-ajs</td>
<td>Dirty River</td>
<td>Womens</td>
<td>.36612</td>
</tr>
<tr>
<td><b>836</b></td>
<td>ZomB's</td>
<td>North Wales</td>
<td>Womens</td>
<td>.36591</td>
</tr>
<tr>
<td><b>837</b></td>
<td>Dread Pirate Rollers</td>
<td>Dread Pirate Rollers</td>
<td>Womens</td>
<td>.36591</td>
</tr>
<tr>
<td><b>838</b></td>
<td>Orléans Roller Derby</td>
<td>Orléans</td>
<td>Womens</td>
<td>.36575</td>
</tr>
<tr>
<td><b>839</b></td>
<td>NOVA Roller Derby</td>
<td>NOVA</td>
<td>Womens</td>
<td>.36569</td>
</tr>
<tr>
<td><b>840</b></td>
<td>Lahti Roller Derby</td>
<td>Lahti</td>
<td>Womens</td>
<td>.36511</td>
</tr>
<tr>
<td><b>841</b></td>
<td>Block Busters</td>
<td>Derby Club le Cres Lattes</td>
<td>Womens</td>
<td>.36496</td>
</tr>
<tr>
<td><b>842</b></td>
<td>York City Derby Dames</td>
<td>York City</td>
<td>Womens</td>
<td>.36480</td>
</tr>
<tr>
<td><b>843</b></td>
<td>Wakey Wheeled Cats</td>
<td>Wakefield</td>
<td>Womens</td>
<td>.36439</td>
</tr>
<tr>
<td><b>844</b></td>
<td>Beat Down</td>
<td>Jersey Shore</td>
<td>Womens</td>
<td>.36422</td>
</tr>
<tr>
<td><b>845</b></td>
<td>The Empire</td>
<td>South Side (NSW)</td>
<td>Womens</td>
<td>.36412</td>
</tr>
<tr>
<td><b>846</b></td>
<td>Carolina Bootleggers</td>
<td>Carolina</td>
<td>Womens</td>
<td>.36410</td>
</tr>
<tr>
<td><b>847</b></td>
<td>Boardwalk Brawlers</td>
<td>Shore Points</td>
<td>Womens</td>
<td>.36378</td>
</tr>
<tr>
<td><b>848</b></td>
<td>Slaughterhouse Derby Girls</td>
<td>Slaughterhouse</td>
<td>Womens</td>
<td>.36377</td>
</tr>
<tr>
<td><b>849</b></td>
<td>Roller Derby Leicester</td>
<td>Leicester</td>
<td>Womens</td>
<td>.36371</td>
</tr>
<tr>
<td><b>850</b></td>
<td>Onslaught</td>
<td>DuPage Derby</td>
<td>Womens</td>
<td>.36363</td>
</tr>
<tr>
<td><b>851</b></td>
<td>Vette City Roller Derby</td>
<td>Vette City</td>
<td>Womens</td>
<td>.36292</td>
</tr>
<tr>
<td><b>852</b></td>
<td>Rocky View Roller Derby Association</td>
<td>Rocky View</td>
<td>Womens</td>
<td>.36256</td>
</tr>
<tr>
<td><b>853</b></td>
<td>Niagara Roller Girls</td>
<td>Niagara</td>
<td>Womens</td>
<td>.36254</td>
</tr>
<tr>
<td><b>854</b></td>
<td>Middle Georgia Derby Demons</td>
<td>Middle Georgia</td>
<td>Womens</td>
<td>.36249</td>
</tr>
<tr>
<td><b>855</b></td>
<td>OKC Outlaws Roller Derby</td>
<td>OKC Outlaws</td>
<td>Womens</td>
<td>.36192</td>
</tr>
<tr>
<td><b>856</b></td>
<td>Roller Derby Creil</td>
<td>Creil</td>
<td>Womens</td>
<td>.36162</td>
</tr>
<tr>
<td><b>857</b></td>
<td>Boomtown Rollers</td>
<td>Boomtown</td>
<td>Womens</td>
<td>.36159</td>
</tr>
<tr>
<td><b>858</b></td>
<td>Orange Crush</td>
<td>Dutchland</td>
<td>Womens</td>
<td>.36131</td>
</tr>
<tr>
<td><b>859</b></td>
<td>Molly's Marauders</td>
<td>Molly Roger</td>
<td>Womens</td>
<td>.36127</td>
</tr>
<tr>
<td><b>860</b></td>
<td>Bloody Bordens</td>
<td>Mass Attack</td>
<td>Womens</td>
<td>.36102</td>
</tr>
<tr>
<td><b>861</b></td>
<td>Roller Derby Tarbes</td>
<td>Tarbes</td>
<td>Womens</td>
<td>.36099</td>
</tr>
<tr>
<td><b>862</b></td>
<td>Waimea Wranglers</td>
<td>Waimea</td>
<td>Womens</td>
<td>.36089</td>
</tr>
<tr>
<td><b>863</b></td>
<td>Alp'n Rockets Roller Derby</td>
<td>Alp'n Rockets</td>
<td>Womens</td>
<td>.36064</td>
</tr>
<tr>
<td><b>864</b></td>
<td>Inner West Roller Derby League</td>
<td>Inner West</td>
<td>Womens</td>
<td>.36030</td>
</tr>
<tr>
<td><b>865</b></td>
<td>Diamond Roughcuts</td>
<td>Diamond Divas</td>
<td>Womens</td>
<td>.36023</td>
</tr>
<tr>
<td><b>866</b></td>
<td>Harbor City Roller Dames</td>
<td>Harbor City</td>
<td>Womens</td>
<td>.36022</td>
</tr>
<tr>
<td><b>867</b></td>
<td>BisMan Bombzillaz</td>
<td>Bombshellz</td>
<td>Womens</td>
<td>.36011</td>
</tr>
<tr>
<td><b>868</b></td>
<td>Violet Femmes</td>
<td>Gem City</td>
<td>Womens</td>
<td>.36007</td>
</tr>
<tr>
<td><b>869</b></td>
<td>Rotten Cherries</td>
<td>Black Rose Rollers</td>
<td>Womens</td>
<td>.35975</td>
</tr>
<tr>
<td><b>870</b></td>
<td>Assault City Roller Derby</td>
<td>Assault City</td>
<td>Womens</td>
<td>.35955</td>
</tr>
<tr>
<td><b>871</b></td>
<td>Glass City B Team</td>
<td>Glass City</td>
<td>Womens</td>
<td>.35928</td>
</tr>
<tr>
<td><b>872</b></td>
<td>North Wales Roller Derby</td>
<td>North Wales</td>
<td>Womens</td>
<td>.35872</td>
</tr>
<tr>
<td><b>873</b></td>
<td>Key West Derby Dames</td>
<td>Key West</td>
<td>Womens</td>
<td>.35857</td>
</tr>
<tr>
<td><b>874</b></td>
<td>Capital Defenders</td>
<td>Red Stick</td>
<td>Womens</td>
<td>.35851</td>
</tr>
<tr>
<td><b>875</b></td>
<td>Emerald Coast Roller Derby</td>
<td>Emerald Coast</td>
<td>Womens</td>
<td>.35838</td>
</tr>
<tr>
<td><b>876</b></td>
<td>River City Dames Of Anarchy</td>
<td>Dames of Anarchy</td>
<td>Womens</td>
<td>.35834</td>
</tr>
<tr>
<td><b>877</b></td>
<td>Zaragoza Roller Derby</td>
<td>Zaragoza</td>
<td>Womens</td>
<td>.35810</td>
</tr>
<tr>
<td><b>878</b></td>
<td>Namur Roller Girls B</td>
<td>Namur</td>
<td>Womens</td>
<td>.35782</td>
</tr>
<tr>
<td><b>879</b></td>
<td>Nickel City Roller Derby</td>
<td>Nickel City</td>
<td>Womens</td>
<td>.35780</td>
</tr>
<tr>
<td><b>880</b></td>
<td>Killa Crew</td>
<td>Killamazoo</td>
<td>Womens</td>
<td>.35740</td>
</tr>
<tr>
<td><b>881</b></td>
<td>Armidale Roller Derby</td>
<td>Armidale</td>
<td>Womens</td>
<td>.35693</td>
</tr>
<tr>
<td><b>882</b></td>
<td>Conroe Roller Derby</td>
<td>Conroe Cutthroats</td>
<td>Womens</td>
<td>.35652</td>
</tr>
<tr>
<td><b>883</b></td>
<td>South Coast Roller Girls</td>
<td>South Coast</td>
<td>Womens</td>
<td>.35632</td>
</tr>
<tr>
<td><b>884</b></td>
<td>Motown Wreckers</td>
<td>Detroit</td>
<td>Womens</td>
<td>.35603</td>
</tr>
<tr>
<td><b>885</b></td>
<td>Greenbrier River Rollers</td>
<td>Greenbrier</td>
<td>Womens</td>
<td>.35588</td>
</tr>
<tr>
<td><b>886</b></td>
<td>B.ADD</td>
<td>Amsterdam</td>
<td>Womens</td>
<td>.35585</td>
</tr>
<tr>
<td><b>887</b></td>
<td>AAA</td>
<td>Omaha</td>
<td>Womens</td>
<td>.35565</td>
</tr>
<tr>
<td><b>888</b></td>
<td>Haunted City Rollers</td>
<td>Haunted City</td>
<td>Womens</td>
<td>.35538</td>
</tr>
<tr>
<td><b>889</b></td>
<td>Beach Brawl SK8R Dolls</td>
<td>Beach Brawl</td>
<td>Womens</td>
<td>.35528</td>
</tr>
<tr>
<td><b>890</b></td>
<td>Seacoast Roller Derby</td>
<td>Poison Pixies</td>
<td>Womens</td>
<td>.35527</td>
</tr>
<tr>
<td><b>891</b></td>
<td>BADD Intentions</td>
<td>Beckley</td>
<td>Womens</td>
<td>.35454</td>
</tr>
<tr>
<td><b>892</b></td>
<td>J-Villains</td>
<td>Jacksonville</td>
<td>Womens</td>
<td>.35448</td>
</tr>
<tr>
<td><b>893</b></td>
<td>Rollerderby Hannover</td>
<td>Hannover</td>
<td>Womens</td>
<td>.35433</td>
</tr>
<tr>
<td><b>894</b></td>
<td>Porto Beasts</td>
<td>Porto</td>
<td>Womens</td>
<td>.35425</td>
</tr>
<tr>
<td><b>895</b></td>
<td>Nasty Nancies</td>
<td>Brisbane City</td>
<td>Womens</td>
<td>.35419</td>
</tr>
<tr>
<td><b>896</b></td>
<td>Biodegradables</td>
<td>Recycled Rollers</td>
<td>Womens</td>
<td>.35319</td>
</tr>
<tr>
<td><b>897</b></td>
<td>Swamp City Sirens</td>
<td>Gainesville</td>
<td>Womens</td>
<td>.35300</td>
</tr>
<tr>
<td><b>898</b></td>
<td>B.M.O. Roller Derby Girls</td>
<td>Brest</td>
<td>Womens</td>
<td>.35258</td>
</tr>
<tr>
<td><b>899</b></td>
<td>Aalborg Roller Derby</td>
<td>Aalborg</td>
<td>Womens</td>
<td>.35252</td>
</tr>
<tr>
<td><b>900</b></td>
<td>Beastie Derby Girls</td>
<td>Reims</td>
<td>Womens</td>
<td>.35251</td>
</tr>
<tr>
<td><b>901</b></td>
<td>St. Cloud Area Roller Dolls</td>
<td>SCAR Dolls</td>
<td>Womens</td>
<td>.35249</td>
</tr>
<tr>
<td><b>902</b></td>
<td>Devil State Derby League</td>
<td>Devil State</td>
<td>Womens</td>
<td>.35175</td>
</tr>
<tr>
<td><b>903</b></td>
<td>Brute Squad</td>
<td>Brandywine</td>
<td>Womens</td>
<td>.35156</td>
</tr>
<tr>
<td><b>904</b></td>
<td>Bomb Squad</td>
<td>Blitz Dames</td>
<td>Womens</td>
<td>.35066</td>
</tr>
<tr>
<td><b>905</b></td>
<td>Natural Disasters</td>
<td>NW Arkansas</td>
<td>Womens</td>
<td>.35022</td>
</tr>
<tr>
<td><b>906</b></td>
<td>Croydon Vice Squad</td>
<td>Croydon</td>
<td>Womens</td>
<td>.35022</td>
</tr>
<tr>
<td><b>907</b></td>
<td>Panthers Miaou</td>
<td>Panthers Graou</td>
<td>Womens</td>
<td>.34986</td>
</tr>
<tr>
<td><b>908</b></td>
<td>Rum City Derby Dolls</td>
<td>Rum City</td>
<td>Womens</td>
<td>.34955</td>
</tr>
<tr>
<td><b>909</b></td>
<td>Black Shucks</td>
<td>Norfolk</td>
<td>Womens</td>
<td>.34907</td>
</tr>
<tr>
<td><b>910</b></td>
<td>Babe City Rollers</td>
<td>Babe City</td>
<td>Womens</td>
<td>.34904</td>
</tr>
<tr>
<td><b>911</b></td>
<td>Gin City Rollers</td>
<td>Plymouth</td>
<td>Womens</td>
<td>.34891</td>
</tr>
<tr>
<td><b>912</b></td>
<td>Harbor Girls B</td>
<td>St. Pauli</td>
<td>Womens</td>
<td>.34853</td>
</tr>
<tr>
<td><b>913</b></td>
<td>Riot Rollers Darmstadt</td>
<td>Darmstadt</td>
<td>Womens</td>
<td>.34755</td>
</tr>
<tr>
<td><b>914</b></td>
<td>Outcast Derby</td>
<td>Outcast</td>
<td>Womens</td>
<td>.34735</td>
</tr>
<tr>
<td><b>915</b></td>
<td>Spindletop Rollergirls</td>
<td>Spindletop</td>
<td>Womens</td>
<td>.34707</td>
</tr>
<tr>
<td><b>916</b></td>
<td>Castle Rock 'n' Rollers</td>
<td>Castle Rock</td>
<td>Womens</td>
<td>.34695</td>
</tr>
<tr>
<td><b>917</b></td>
<td>Acadiana Roller Girls</td>
<td>Acadiana</td>
<td>Womens</td>
<td>.34668</td>
</tr>
<tr>
<td><b>918</b></td>
<td>Eastbourne Roller Derby (Womens)</td>
<td>Eastbourne Womens</td>
<td>Womens</td>
<td>.34667</td>
</tr>
<tr>
<td><b>919</b></td>
<td>Severn Roller Torrent</td>
<td>Severn</td>
<td>Womens</td>
<td>.34633</td>
</tr>
<tr>
<td><b>920</b></td>
<td>Seven Valley Rollers</td>
<td>7 Valley</td>
<td>Womens</td>
<td>.34539</td>
</tr>
<tr>
<td><b>921</b></td>
<td>Bunbury Roller Derby</td>
<td>Bunbury</td>
<td>Womens</td>
<td>.34526</td>
</tr>
<tr>
<td><b>922</b></td>
<td>Freaky Mons'ter Derby Ladies</td>
<td>Mons</td>
<td>Womens</td>
<td>.34515</td>
</tr>
<tr>
<td><b>923</b></td>
<td>Nancy Roller Derby</td>
<td>Nancy</td>
<td>Womens</td>
<td>.34496</td>
</tr>
<tr>
<td><b>924</b></td>
<td>Bluestockings</td>
<td>Ithaca</td>
<td>Womens</td>
<td>.34494</td>
</tr>
<tr>
<td><b>925</b></td>
<td>Roller Derby Bordeaux</td>
<td>Bordeaux</td>
<td>Womens</td>
<td>.34401</td>
</tr>
<tr>
<td><b>926</b></td>
<td>Blue Mountains Roller Derby League</td>
<td>Blue Mountains</td>
<td>Womens</td>
<td>.34388</td>
</tr>
<tr>
<td><b>927</b></td>
<td>Hurricane Alley Roller Derby</td>
<td>Hurricane Alley</td>
<td>Womens</td>
<td>.34361</td>
</tr>
<tr>
<td><b>928</b></td>
<td>Roller Derby Karlsruhe</td>
<td>Karlsruhe</td>
<td>Womens</td>
<td>.34322</td>
</tr>
<tr>
<td><b>929</b></td>
<td>301 Derby Dames</td>
<td>301 Derby</td>
<td>Womens</td>
<td>.34230</td>
</tr>
<tr>
<td><b>930</b></td>
<td>Sugar Sands Roller Dolls</td>
<td>Sugar Sands</td>
<td>Womens</td>
<td>.34218</td>
</tr>
<tr>
<td><b>931</b></td>
<td>Roller Derby Dijon</td>
<td>Dijon</td>
<td>Womens</td>
<td>.34164</td>
</tr>
<tr>
<td><b>932</b></td>
<td>Denali Destroyers</td>
<td>Destroyer Dolls</td>
<td>Womens</td>
<td>.34117</td>
</tr>
<tr>
<td><b>933</b></td>
<td>Wrangell Roller Derby</td>
<td>Wrangell</td>
<td>Womens</td>
<td>.34109</td>
</tr>
<tr>
<td><b>934</b></td>
<td>Upstate Roller Girl Evolution</td>
<td>URGE</td>
<td>Womens</td>
<td>.34063</td>
</tr>
<tr>
<td><b>935</b></td>
<td>Heartland Havoc</td>
<td>ICT</td>
<td>Womens</td>
<td>.34056</td>
</tr>
<tr>
<td><b>936</b></td>
<td>Muncie MissFits</td>
<td>Cornfed</td>
<td>Womens</td>
<td>.33962</td>
</tr>
<tr>
<td><b>937</b></td>
<td>Slay Belles</td>
<td>Central City</td>
<td>Womens</td>
<td>.33961</td>
</tr>
<tr>
<td><b>938</b></td>
<td>East Lansing Roller Derby</td>
<td>East Lansing</td>
<td>Womens</td>
<td>.33959</td>
</tr>
<tr>
<td><b>939</b></td>
<td>Heart of Appalachia Roller Derby</td>
<td>Heart of Appalachia</td>
<td>Womens</td>
<td>.33941</td>
</tr>
<tr>
<td><b>940</b></td>
<td>Los Alamos Derby Dames</td>
<td>Los Alamos</td>
<td>Womens</td>
<td>.33917</td>
</tr>
<tr>
<td><b>941</b></td>
<td>St. Albert Heavenly Rollers Derby</td>
<td>Heavenly Rollers</td>
<td>Womens</td>
<td>.33912</td>
</tr>
<tr>
<td><b>942</b></td>
<td>Northern Allegheny Roller Derby</td>
<td>Northern Allegheny</td>
<td>Womens</td>
<td>.33903</td>
</tr>
<tr>
<td><b>943</b></td>
<td>Diamond City Roller Derby</td>
<td>Diamond City</td>
<td>Womens</td>
<td>.33898</td>
</tr>
<tr>
<td><b>944</b></td>
<td>South Central Roller Girls</td>
<td>South Central</td>
<td>Womens</td>
<td>.33868</td>
</tr>
<tr>
<td><b>945</b></td>
<td>Bux-Mont Roller Derby Dolls</td>
<td>Bux-Mont</td>
<td>Womens</td>
<td>.33821</td>
</tr>
<tr>
<td><b>946</b></td>
<td>Downriver Muscle</td>
<td>Downriver</td>
<td>Womens</td>
<td>.33741</td>
</tr>
<tr>
<td><b>947</b></td>
<td>Garden Island Renegade Rollerz</td>
<td>G.I. Renegade Rollerz</td>
<td>Womens</td>
<td>.33706</td>
</tr>
<tr>
<td><b>948</b></td>
<td>The Jokers</td>
<td>The Parliament of Pain</td>
<td>Womens</td>
<td>.33698</td>
</tr>
<tr>
<td><b>949</b></td>
<td>Sarnia Roller Derby League</td>
<td>Sarnia</td>
<td>Womens</td>
<td>.33697</td>
</tr>
<tr>
<td><b>950</b></td>
<td>Rotterdam Killer Bees</td>
<td>Rotterdam</td>
<td>Womens</td>
<td>.33694</td>
</tr>
<tr>
<td><b>951</b></td>
<td>Orlando Roller Derby B</td>
<td>Psycho City</td>
<td>Womens</td>
<td>.33670</td>
</tr>
<tr>
<td><b>952</b></td>
<td>Rollergirls Of Central Kentucky</td>
<td>R.O.C.K.</td>
<td>Womens</td>
<td>.33622</td>
</tr>
<tr>
<td><b>953</b></td>
<td>New River Knockouts</td>
<td>New River</td>
<td>Womens</td>
<td>.33616</td>
</tr>
<tr>
<td><b>954</b></td>
<td>Festival City Rollergirls</td>
<td>Festival City</td>
<td>Womens</td>
<td>.33532</td>
</tr>
<tr>
<td><b>955</b></td>
<td>Roller Derby Madrid B</td>
<td>Madrid</td>
<td>Womens</td>
<td>.33493</td>
</tr>
<tr>
<td><b>956</b></td>
<td>Capital City Roller Girls</td>
<td>Capital City</td>
<td>Womens</td>
<td>.33470</td>
</tr>
<tr>
<td><b>957</b></td>
<td>Third Alarm</td>
<td>Naptown</td>
<td>Womens</td>
<td>.33364</td>
</tr>
<tr>
<td><b>958</b></td>
<td>The York Minxters</td>
<td>York</td>
<td>Womens</td>
<td>.33352</td>
</tr>
<tr>
<td><b>959</b></td>
<td>New Generation</td>
<td>Antwerp</td>
<td>Womens</td>
<td>.33348</td>
</tr>
<tr>
<td><b>960</b></td>
<td>Reaper Roller Derby</td>
<td>Reaper</td>
<td>Womens</td>
<td>.33342</td>
</tr>
<tr>
<td><b>961</b></td>
<td>Tulsa Derby League</td>
<td>Tulsa Derby Brigade</td>
<td>Womens</td>
<td>.33333</td>
</tr>
<tr>
<td><b>962</b></td>
<td>Gillette Roller Derby</td>
<td>Miners' Daughters</td>
<td>Womens</td>
<td>.33267</td>
</tr>
<tr>
<td><b>963</b></td>
<td>Jailbreak Betties</td>
<td>Tallahassee</td>
<td>Womens</td>
<td>.33256</td>
</tr>
<tr>
<td><b>964</b></td>
<td>Keweenaw Roller Girls</td>
<td>Keweenaw</td>
<td>Womens</td>
<td>.33243</td>
</tr>
<tr>
<td><b>965</b></td>
<td>Udder Team</td>
<td>Milton Keynes</td>
<td>Womens</td>
<td>.33213</td>
</tr>
<tr>
<td><b>966</b></td>
<td>Jyväskylä Roller Derby</td>
<td>Jyväskylä</td>
<td>Womens</td>
<td>.33207</td>
</tr>
<tr>
<td><b>967</b></td>
<td>Baronnes Von Schlass</td>
<td>Switchblade</td>
<td>Womens</td>
<td>.33167</td>
</tr>
<tr>
<td><b>968</b></td>
<td>Mississippi Rollergirls</td>
<td>Mississippi Rollergirls</td>
<td>Womens</td>
<td>.33118</td>
</tr>
<tr>
<td><b>969</b></td>
<td>Convicts</td>
<td>Richter City</td>
<td>Womens</td>
<td>.33102</td>
</tr>
<tr>
<td><b>970</b></td>
<td>Southern Illinois Roller Girls</td>
<td>So Ill</td>
<td>Womens</td>
<td>.33047</td>
</tr>
<tr>
<td><b>971</b></td>
<td>Breaking Bears</td>
<td>Bear City</td>
<td>Womens</td>
<td>.32937</td>
</tr>
<tr>
<td><b>972</b></td>
<td>Sulphur City Steam Rollers</td>
<td>Sulphur City</td>
<td>Womens</td>
<td>.32916</td>
</tr>
<tr>
<td><b>973</b></td>
<td>Confluence Crush Roller Derby</td>
<td>Confluence</td>
<td>Womens</td>
<td>.32910</td>
</tr>
<tr>
<td><b>974</b></td>
<td>Western Sydney Rollers</td>
<td>Western Sydney</td>
<td>Womens</td>
<td>.32906</td>
</tr>
<tr>
<td><b>975</b></td>
<td>Roller Derby Rennes - équipe B</td>
<td>Rennes</td>
<td>Womens</td>
<td>.32899</td>
</tr>
<tr>
<td><b>976</b></td>
<td>Grey Bruce Roller Derby</td>
<td>Grey Bruce</td>
<td>Womens</td>
<td>.32862</td>
</tr>
<tr>
<td><b>977</b></td>
<td>C-kasetti</td>
<td>Helsinki</td>
<td>Womens</td>
<td>.32837</td>
</tr>
<tr>
<td><b>978</b></td>
<td>Stone Cold Foxes</td>
<td>Stone Cold Foxes</td>
<td>Womens</td>
<td>.32812</td>
</tr>
<tr>
<td><b>979</b></td>
<td>Dothan Roller Derby</td>
<td>Dothan</td>
<td>Womens</td>
<td>.32785</td>
</tr>
<tr>
<td><b>980</b></td>
<td>Bazooka Janes</td>
<td>Capital City</td>
<td>Womens</td>
<td>.32700</td>
</tr>
<tr>
<td><b>981</b></td>
<td>Yellow Shovemarines</td>
<td>Liverpool</td>
<td>Womens</td>
<td>.32651</td>
</tr>
<tr>
<td><b>982</b></td>
<td>Petersburg Ragnarök Rollers</td>
<td>Petersburg Ragnarök Rollers</td>
<td>Womens</td>
<td>.32637</td>
</tr>
<tr>
<td><b>983</b></td>
<td>Lisboa Roller Derby</td>
<td>Lisboa</td>
<td>Womens</td>
<td>.32632</td>
</tr>
<tr>
<td><b>984</b></td>
<td>Roller Derby Lorient</td>
<td>Lorient</td>
<td>Womens</td>
<td>.32569</td>
</tr>
<tr>
<td><b>985</b></td>
<td>Tiger Lilies</td>
<td>Wirral (Women's)</td>
<td>Womens</td>
<td>.32537</td>
</tr>
<tr>
<td><b>986</b></td>
<td>Gapland Rollers</td>
<td>Gapland</td>
<td>Womens</td>
<td>.32534</td>
</tr>
<tr>
<td><b>987</b></td>
<td>Brighton Roller Dollz</td>
<td>Brighton (MI)</td>
<td>Womens</td>
<td>.32516</td>
</tr>
<tr>
<td><b>988</b></td>
<td>Pacific Roller Derby</td>
<td>Pacific</td>
<td>Womens</td>
<td>.32491</td>
</tr>
<tr>
<td><b>989</b></td>
<td>Suck City Rock 'n Roller Dolls</td>
<td>Suck City</td>
<td>Womens</td>
<td>.32475</td>
</tr>
<tr>
<td><b>990</b></td>
<td>PLAP City Rollers</td>
<td>PLAP City</td>
<td>Womens</td>
<td>.32414</td>
</tr>
<tr>
<td><b>991</b></td>
<td>Battlefield Roller Derby</td>
<td>Battlefield</td>
<td>Womens</td>
<td>.32412</td>
</tr>
<tr>
<td><b>992</b></td>
<td>The Bet Lynch Mob</td>
<td>Rainy City (UK)</td>
<td>Womens</td>
<td>.32375</td>
</tr>
<tr>
<td><b>993</b></td>
<td>Mississippi Brawl Stars</td>
<td>Brawl Stars</td>
<td>Womens</td>
<td>.32371</td>
</tr>
<tr>
<td><b>994</b></td>
<td>Grim Reavers</td>
<td>Grim Reavers</td>
<td>Womens</td>
<td>.32335</td>
</tr>
<tr>
<td><b>995</b></td>
<td>Counterstrike</td>
<td>Greensboro</td>
<td>Womens</td>
<td>.32299</td>
</tr>
<tr>
<td><b>996</b></td>
<td>Taxider'Biches Thonon</td>
<td>Taxider'Biches</td>
<td>Womens</td>
<td>.32296</td>
</tr>
<tr>
<td><b>997</b></td>
<td>Blood, Bath, and Beyond</td>
<td>Bath City</td>
<td>Womens</td>
<td>.32288</td>
</tr>
<tr>
<td><b>998</b></td>
<td>Central Michigan Roller Derby</td>
<td>Central Michigan</td>
<td>Womens</td>
<td>.32262</td>
</tr>
<tr>
<td><b>999</b></td>
<td>Hammer City Harlots</td>
<td>Hammer City</td>
<td>Womens</td>
<td>.32255</td>
</tr>
<tr>
<td><b>1000</b></td>
<td>Riot City Ravens</td>
<td>Riot City Ravens</td>
<td>Womens</td>
<td>.32154</td>
</tr>
<tr>
<td><b>1001</b></td>
<td>Trouble Makers</td>
<td>Charm City</td>
<td>Womens</td>
<td>.32134</td>
</tr>
<tr>
<td><b>1002</b></td>
<td>Roller Derby Calaisis (Women's)</td>
<td>Calais (Women's)</td>
<td>Womens</td>
<td>.32126</td>
</tr>
<tr>
<td><b>1003</b></td>
<td>Renfrew County Roller Derby</td>
<td>Renfrew County</td>
<td>Womens</td>
<td>.32074</td>
</tr>
<tr>
<td><b>1004</b></td>
<td>Copper City Queens Roller Derby</td>
<td>Copper City</td>
<td>Womens</td>
<td>.32028</td>
</tr>
<tr>
<td><b>1005</b></td>
<td>Roller Derby Sherbrooke</td>
<td>Sherbrooke</td>
<td>Womens</td>
<td>.31994</td>
</tr>
<tr>
<td><b>1006</b></td>
<td>Roller Derby Genève</td>
<td>Leman'Wheels</td>
<td>Womens</td>
<td>.31981</td>
</tr>
<tr>
<td><b>1007</b></td>
<td>Mansfield Roller Derby</td>
<td>Mansfield</td>
<td>Womens</td>
<td>.31914</td>
</tr>
<tr>
<td><b>1008</b></td>
<td>Lightning Broads</td>
<td>Oklahoma City</td>
<td>Womens</td>
<td>.31883</td>
</tr>
<tr>
<td><b>1009</b></td>
<td>Rocktown Rollers</td>
<td>Rocktown</td>
<td>Womens</td>
<td>.31865</td>
</tr>
<tr>
<td><b>1010</b></td>
<td>Goosetown Roller Girls</td>
<td>Goosetown</td>
<td>Womens</td>
<td>.31770</td>
</tr>
<tr>
<td><b>1011</b></td>
<td>Virgin Marys</td>
<td>Geelong</td>
<td>Womens</td>
<td>.31763</td>
</tr>
<tr>
<td><b>1012</b></td>
<td>Shanghaied Roller Dolls</td>
<td>Shanghaied</td>
<td>Womens</td>
<td>.31692</td>
</tr>
<tr>
<td><b>1013</b></td>
<td>Kill Devil Derby Brigade</td>
<td>Kill Devil</td>
<td>Womens</td>
<td>.31672</td>
</tr>
<tr>
<td><b>1014</b></td>
<td>Albuquerque Roller Derby (Womens)</td>
<td>Albuquerque Roller Derby(W)</td>
<td>Womens</td>
<td>.31599</td>
</tr>
<tr>
<td><b>1015</b></td>
<td>Roll'in Tarn Roller Derby</td>
<td>Roll'in Tarn</td>
<td>Womens</td>
<td>.31559</td>
</tr>
<tr>
<td><b>1016</b></td>
<td>Arnhem Fallen Angels</td>
<td>Arnhem</td>
<td>Womens</td>
<td>.31554</td>
</tr>
<tr>
<td><b>1017</b></td>
<td>Killa Geishas of Misawa</td>
<td>Killa Geishas</td>
<td>Womens</td>
<td>.31430</td>
</tr>
<tr>
<td><b>1018</b></td>
<td>Plan B</td>
<td>Dock City</td>
<td>Womens</td>
<td>.31418</td>
</tr>
<tr>
<td><b>1019</b></td>
<td>Shee Devils</td>
<td>Sitka</td>
<td>Womens</td>
<td>.31414</td>
</tr>
<tr>
<td><b>1020</b></td>
<td>Southern Delaware Rollergirls</td>
<td>Southern Delaware</td>
<td>Womens</td>
<td>.31400</td>
</tr>
<tr>
<td><b>1021</b></td>
<td>Porvoo Roller Derby</td>
<td>Porvoo</td>
<td>Womens</td>
<td>.31355</td>
</tr>
<tr>
<td><b>1022</b></td>
<td>Paris Hockey Club</td>
<td>Les Gueuses A</td>
<td>Womens</td>
<td>.31347</td>
</tr>
<tr>
<td><b>1023</b></td>
<td>Roskilde Roller Derby</td>
<td>Roskilde</td>
<td>Womens</td>
<td>.31331</td>
</tr>
<tr>
<td><b>1024</b></td>
<td>Badda Bings</td>
<td>Swamp City</td>
<td>Womens</td>
<td>.31301</td>
</tr>
<tr>
<td><b>1025</b></td>
<td>Nidaros Killer B's</td>
<td>Nidaros</td>
<td>Womens</td>
<td>.31286</td>
</tr>
<tr>
<td><b>1026</b></td>
<td>Rust Belt Rollers</td>
<td>Little Steel Derby Girls</td>
<td>Womens</td>
<td>.31243</td>
</tr>
<tr>
<td><b>1027</b></td>
<td>Roller Derby Rimouski</td>
<td>Rimouski</td>
<td>Womens</td>
<td>.31233</td>
</tr>
<tr>
<td><b>1028</b></td>
<td>Vienna Beasts</td>
<td>Vienna</td>
<td>Womens</td>
<td>.31187</td>
</tr>
<tr>
<td><b>1029</b></td>
<td>Belleville Roller Derby</td>
<td>Belleville</td>
<td>Womens</td>
<td>.31180</td>
</tr>
<tr>
<td><b>1030</b></td>
<td>Scarlet Fever</td>
<td>Wheat City</td>
<td>Womens</td>
<td>.31148</td>
</tr>
<tr>
<td><b>1031</b></td>
<td>Sintral Florida Derby Demons</td>
<td>Sintral</td>
<td>Womens</td>
<td>.31133</td>
</tr>
<tr>
<td><b>1032</b></td>
<td>Team Griffin</td>
<td>Northern Brisbane</td>
<td>Womens</td>
<td>.31092</td>
</tr>
<tr>
<td><b>1033</b></td>
<td>Bath Roman Rollers</td>
<td>Bath Spartans</td>
<td>Womens</td>
<td>.31075</td>
</tr>
<tr>
<td><b>1034</b></td>
<td>Kuopio Roller Derby</td>
<td>Kuopio</td>
<td>Womens</td>
<td>.31036</td>
</tr>
<tr>
<td><b>1035</b></td>
<td>Rabbit Skulls Roller Derby Avignon</td>
<td>Rabbit Skulls</td>
<td>Womens</td>
<td>.30992</td>
</tr>
<tr>
<td><b>1036</b></td>
<td>Herculadies</td>
<td>Hellions</td>
<td>Womens</td>
<td>.30984</td>
</tr>
<tr>
<td><b>1037</b></td>
<td>Howlin' Rolls</td>
<td>Tampere</td>
<td>Womens</td>
<td>.30970</td>
</tr>
<tr>
<td><b>1038</b></td>
<td>South Simcoe Rebel Rollers</td>
<td>South Simcoe</td>
<td>Womens</td>
<td>.30917</td>
</tr>
<tr>
<td><b>1039</b></td>
<td>B-Dazzlers</td>
<td>Charlotte</td>
<td>Womens</td>
<td>.30910</td>
</tr>
<tr>
<td><b>1040</b></td>
<td>Terrorz of Tiny Towns</td>
<td>Diesel Dollz</td>
<td>Womens</td>
<td>.30864</td>
</tr>
<tr>
<td><b>1041</b></td>
<td>Bodø Roller Derby</td>
<td>Bodø</td>
<td>Womens</td>
<td>.30859</td>
</tr>
<tr>
<td><b>1042</b></td>
<td>Oxford Wheels of Gory Roller Derby</td>
<td>Wheels of Gory</td>
<td>Womens</td>
<td>.30838</td>
</tr>
<tr>
<td><b>1043</b></td>
<td>Second Line</td>
<td>Big Easy</td>
<td>Womens</td>
<td>.30814</td>
</tr>
<tr>
<td><b>1044</b></td>
<td>Key City Roller Derby</td>
<td>Key City</td>
<td>Womens</td>
<td>.30728</td>
</tr>
<tr>
<td><b>1045</b></td>
<td>Lindsay Roller Derby</td>
<td>Lindsay</td>
<td>Womens</td>
<td>.30702</td>
</tr>
<tr>
<td><b>1046</b></td>
<td>Sandusky Rollergirls</td>
<td>Sandusky</td>
<td>Womens</td>
<td>.30696</td>
</tr>
<tr>
<td><b>1047</b></td>
<td>Les Gueuses de Pigalle B</td>
<td>Les Gueuses A</td>
<td>Womens</td>
<td>.30691</td>
</tr>
<tr>
<td><b>1048</b></td>
<td>Redcliff Roller Derby Association</td>
<td>Redcliff</td>
<td>Womens</td>
<td>.30656</td>
</tr>
<tr>
<td><b>1049</b></td>
<td>Roller Derby Torino</td>
<td>Torino</td>
<td>Womens</td>
<td>.30649</td>
</tr>
<tr>
<td><b>1050</b></td>
<td>La Barbaque</td>
<td>Quads de Paris</td>
<td>Womens</td>
<td>.30624</td>
</tr>
<tr>
<td><b>1051</b></td>
<td>Plymouth City Roller Derby</td>
<td>Plymouth</td>
<td>Womens</td>
<td>.30622</td>
</tr>
<tr>
<td><b>1052</b></td>
<td>Brawlers</td>
<td>Hard Knox</td>
<td>Womens</td>
<td>.30600</td>
</tr>
<tr>
<td><b>1053</b></td>
<td>Castres Roller Derby</td>
<td>Castres</td>
<td>Womens</td>
<td>.30583</td>
</tr>
<tr>
<td><b>1054</b></td>
<td>Diamond State Rollergirls</td>
<td>Diamond State</td>
<td>Womens</td>
<td>.30552</td>
</tr>
<tr>
<td><b>1055</b></td>
<td>Van Diemen Rollers</td>
<td>Van Diemen</td>
<td>Womens</td>
<td>.30550</td>
</tr>
<tr>
<td><b>1056</b></td>
<td>Two Rivers Roller Derby B Team</td>
<td>Two Rivers</td>
<td>Womens</td>
<td>.30472</td>
</tr>
<tr>
<td><b>1057</b></td>
<td>Queen's Court</td>
<td>Queen City</td>
<td>Womens</td>
<td>.30459</td>
</tr>
<tr>
<td><b>1058</b></td>
<td>Narbonne Roller Sports</td>
<td>Head Hunters</td>
<td>Womens</td>
<td>.30457</td>
</tr>
<tr>
<td><b>1059</b></td>
<td>MidState Mayhem Roller Derby</td>
<td>MidState Mayhem</td>
<td>Womens</td>
<td>.30456</td>
</tr>
<tr>
<td><b>1060</b></td>
<td>Rebel Alliance</td>
<td>Melbourne Northside</td>
<td>Womens</td>
<td>.30415</td>
</tr>
<tr>
<td><b>1061</b></td>
<td>Black Thunders Madrid (Women's)</td>
<td>Black Thunders</td>
<td>Womens</td>
<td>.30405</td>
</tr>
<tr>
<td><b>1062</b></td>
<td>Wheels of Pain</td>
<td>Ohio Valley</td>
<td>Womens</td>
<td>.30380</td>
</tr>
<tr>
<td><b>1063</b></td>
<td>Roller Derby Chalon</td>
<td>Roller Derby Chalon</td>
<td>Womens</td>
<td>.30376</td>
</tr>
<tr>
<td><b>1064</b></td>
<td>Macomb Bombshells</td>
<td>Macomb</td>
<td>Womens</td>
<td>.30360</td>
</tr>
<tr>
<td><b>1065</b></td>
<td>Roller Derby Palermo</td>
<td>Poison Kittens</td>
<td>Womens</td>
<td>.30318</td>
</tr>
<tr>
<td><b>1066</b></td>
<td>Central California Area Derby</td>
<td>Central California</td>
<td>Womens</td>
<td>.30194</td>
</tr>
<tr>
<td><b>1067</b></td>
<td>A-Town Roller Derby</td>
<td>A-Town</td>
<td>Womens</td>
<td>.30181</td>
</tr>
<tr>
<td><b>1068</b></td>
<td>Arctic Roller Derby</td>
<td>Arctic</td>
<td>Womens</td>
<td>.30085</td>
</tr>
<tr>
<td><b>1069</b></td>
<td>VooDoo Roller Dollies</td>
<td>Voodoo Roller Dollies</td>
<td>Womens</td>
<td>.30040</td>
</tr>
<tr>
<td><b>1070</b></td>
<td>Lothian Derby Dolls</td>
<td>Lothian</td>
<td>Womens</td>
<td>.30033</td>
</tr>
<tr>
<td><b>1071</b></td>
<td>Roller Derby La Rochelle</td>
<td>La Rochelle</td>
<td>Womens</td>
<td>.29988</td>
</tr>
<tr>
<td><b>1072</b></td>
<td>Evolution Roller Derby</td>
<td>Evolution</td>
<td>Womens</td>
<td>.29966</td>
</tr>
<tr>
<td><b>1073</b></td>
<td>Portside Pirates</td>
<td>Fog City</td>
<td>Womens</td>
<td>.29891</td>
</tr>
<tr>
<td><b>1074</b></td>
<td>Darwin Rollergirls</td>
<td>Darwin</td>
<td>Womens</td>
<td>.29876</td>
</tr>
<tr>
<td><b>1075</b></td>
<td>Hellfire Harlots B Team</td>
<td>Nottingham Hellfire Harlots</td>
<td>Womens</td>
<td>.29807</td>
</tr>
<tr>
<td><b>1076</b></td>
<td>Ladies' Death and Derby Society</td>
<td>Ladies D&amp;D Society</td>
<td>Womens</td>
<td>.29675</td>
</tr>
<tr>
<td><b>1077</b></td>
<td>Zombie Rollergirlz Münster</td>
<td>Münster</td>
<td>Womens</td>
<td>.29658</td>
</tr>
<tr>
<td><b>1078</b></td>
<td>Ypsilanti Vigilantes</td>
<td>Ann Arbor</td>
<td>Womens</td>
<td>.29644</td>
</tr>
<tr>
<td><b>1079</b></td>
<td>Preston Roller Girls B Team</td>
<td>Preston</td>
<td>Womens</td>
<td>.29611</td>
</tr>
<tr>
<td><b>1080</b></td>
<td>Grimshaw Grim Reapers Roller Derby Team</td>
<td>Grimshaw</td>
<td>Womens</td>
<td>.29597</td>
</tr>
<tr>
<td><b>1081</b></td>
<td>The Bad Seeds</td>
<td>Stuttgart Valley</td>
<td>Womens</td>
<td>.29551</td>
</tr>
<tr>
<td><b>1082</b></td>
<td>Plan B</td>
<td>State College</td>
<td>Womens</td>
<td>.29530</td>
</tr>
<tr>
<td><b>1083</b></td>
<td>GrassRoots Rollergirls</td>
<td>GrassRoots</td>
<td>Womens</td>
<td>.29522</td>
</tr>
<tr>
<td><b>1084</b></td>
<td>Cheshire Hellcats Roller Derby</td>
<td>Cheshire</td>
<td>Womens</td>
<td>.29514</td>
</tr>
<tr>
<td><b>1085</b></td>
<td>Bradentucky Bombers</td>
<td>Bradentucky</td>
<td>Womens</td>
<td>.29498</td>
</tr>
<tr>
<td><b>1086</b></td>
<td>Les Petroleuses</td>
<td>Caen</td>
<td>Womens</td>
<td>.29483</td>
</tr>
<tr>
<td><b>1087</b></td>
<td>Backlash</td>
<td>Punishers</td>
<td>Womens</td>
<td>.29473</td>
</tr>
<tr>
<td><b>1088</b></td>
<td>Southern Maryland Roller Derby</td>
<td>Southern Maryland</td>
<td>Womens</td>
<td>.29439</td>
</tr>
<tr>
<td><b>1089</b></td>
<td>Oisans Roller Derby</td>
<td>Les Sc'Alpes Hell</td>
<td>Womens</td>
<td>.29437</td>
</tr>
<tr>
<td><b>1090</b></td>
<td>Roller Derby Côte Basque</td>
<td>Côte Basque</td>
<td>Womens</td>
<td>.29434</td>
</tr>
<tr>
<td><b>1091</b></td>
<td>Ardèche rollers girl</td>
<td>Ardèche</td>
<td>Womens</td>
<td>.29352</td>
</tr>
<tr>
<td><b>1092</b></td>
<td>Aurora Boriellas Roller Derby</td>
<td>Aurora Boriellas</td>
<td>Womens</td>
<td>.29305</td>
</tr>
<tr>
<td><b>1093</b></td>
<td>Peoria Push Derby Dames</td>
<td>Peoria Push</td>
<td>Womens</td>
<td>.29245</td>
</tr>
<tr>
<td><b>1094</b></td>
<td>Wicomikazis</td>
<td>Salisbury</td>
<td>Womens</td>
<td>.29209</td>
</tr>
<tr>
<td><b>1095</b></td>
<td>Roller Skating Montreuil</td>
<td>Montreuil</td>
<td>Womens</td>
<td>.29185</td>
</tr>
<tr>
<td><b>1096</b></td>
<td>Mankato Area Derby Girls</td>
<td>Mankato</td>
<td>Womens</td>
<td>.29173</td>
</tr>
<tr>
<td><b>1097</b></td>
<td>The Banshees</td>
<td>South Sea</td>
<td>Womens</td>
<td>.29146</td>
</tr>
<tr>
<td><b>1098</b></td>
<td>Palmetto State Rollergirls</td>
<td>Palmetto State</td>
<td>Womens</td>
<td>.29089</td>
</tr>
<tr>
<td><b>1099</b></td>
<td>New Hampshire Roller Derby Cherry Bombs</td>
<td>New Hampshire</td>
<td>Womens</td>
<td>.29088</td>
</tr>
<tr>
<td><b>1100</b></td>
<td>Broome County Rollers</td>
<td>BC Rollers</td>
<td>Womens</td>
<td>.28922</td>
</tr>
<tr>
<td><b>1101</b></td>
<td>Capital Brawlers</td>
<td>Canberra</td>
<td>Womens</td>
<td>.28869</td>
</tr>
<tr>
<td><b>1102</b></td>
<td>Smitten Kittens</td>
<td>Confluence</td>
<td>Womens</td>
<td>.28751</td>
</tr>
<tr>
<td><b>1103</b></td>
<td>Cannon Brawlers</td>
<td>Mason-Dixon</td>
<td>Womens</td>
<td>.28686</td>
</tr>
<tr>
<td><b>1104</b></td>
<td>Warrin' Wrecking Dolls</td>
<td>Wrecking Dolls</td>
<td>Womens</td>
<td>.28677</td>
</tr>
<tr>
<td><b>1105</b></td>
<td>Bombshell Battalion</td>
<td>Renegade</td>
<td>Womens</td>
<td>.28582</td>
</tr>
<tr>
<td><b>1106</b></td>
<td>Ayrshire Roller Derby</td>
<td>Ayrshire</td>
<td>Womens</td>
<td>.28541</td>
</tr>
<tr>
<td><b>1107</b></td>
<td>Otway Derby Dolls</td>
<td>Otway</td>
<td>Womens</td>
<td>.28528</td>
</tr>
<tr>
<td><b>1108</b></td>
<td>Roller Derby Russia</td>
<td>St. Petersburg</td>
<td>Womens</td>
<td>.28458</td>
</tr>
<tr>
<td><b>1109</b></td>
<td>Port City Roller Derby</td>
<td>Port City</td>
<td>Womens</td>
<td>.28435</td>
</tr>
<tr>
<td><b>1110</b></td>
<td>Shipwreckers</td>
<td>Harbor City</td>
<td>Womens</td>
<td>.28374</td>
</tr>
<tr>
<td><b>1111</b></td>
<td>Crucibelles</td>
<td>Sheffield</td>
<td>Womens</td>
<td>.28363</td>
</tr>
<tr>
<td><b>1112</b></td>
<td>South Island Sirens Roller Derby League</td>
<td>South Island Sirens</td>
<td>Womens</td>
<td>.28326</td>
</tr>
<tr>
<td><b>1113</b></td>
<td>Far North Derby DollZ</td>
<td>Far North</td>
<td>Womens</td>
<td>.28285</td>
</tr>
<tr>
<td><b>1114</b></td>
<td>Gulf Coast Rollergirls</td>
<td>Lafitte's Ladies</td>
<td>Womens</td>
<td>.28220</td>
</tr>
<tr>
<td><b>1115</b></td>
<td>Wagga Derby Dolls</td>
<td>Wagga</td>
<td>Womens</td>
<td>.28215</td>
</tr>
<tr>
<td><b>1116</b></td>
<td>Central Vermont Roller Derby</td>
<td>Central VT Roller Derby</td>
<td>Womens</td>
<td>.28168</td>
</tr>
<tr>
<td><b>1117</b></td>
<td>Backyard Bullies</td>
<td>Suburbia</td>
<td>Womens</td>
<td>.28068</td>
</tr>
<tr>
<td><b>1118</b></td>
<td>Rebel Army Derby</td>
<td>Rebel Army</td>
<td>Womens</td>
<td>.27989</td>
</tr>
<tr>
<td><b>1119</b></td>
<td>Party Crashers</td>
<td>Circle City</td>
<td>Womens</td>
<td>.27931</td>
</tr>
<tr>
<td><b>1120</b></td>
<td>Les Pisseuses Malefiques</td>
<td>Les Pisseuses</td>
<td>Womens</td>
<td>.27929</td>
</tr>
<tr>
<td><b>1121</b></td>
<td>Misdemeanors</td>
<td>Ft. Myers</td>
<td>Womens</td>
<td>.27889</td>
</tr>
<tr>
<td><b>1122</b></td>
<td>Mid Atlantic Roller Derby</td>
<td>Mid Atlantic</td>
<td>Womens</td>
<td>.27852</td>
</tr>
<tr>
<td><b>1123</b></td>
<td>Nottingham Roller Girls B</td>
<td>Nottingham</td>
<td>Womens</td>
<td>.27812</td>
</tr>
<tr>
<td><b>1124</b></td>
<td>Reckoning</td>
<td>Texas</td>
<td>Womens</td>
<td>.27605</td>
</tr>
<tr>
<td><b>1125</b></td>
<td>Rapid Assault</td>
<td>Grand Raggidy</td>
<td>Womens</td>
<td>.27546</td>
</tr>
<tr>
<td><b>1126</b></td>
<td>Farmers</td>
<td>Durham (Canada)</td>
<td>Womens</td>
<td>.27478</td>
</tr>
<tr>
<td><b>1127</b></td>
<td>Murder City Roller Girls</td>
<td>Murder City</td>
<td>Womens</td>
<td>.27455</td>
</tr>
<tr>
<td><b>1128</b></td>
<td>Southshire Roller Derby</td>
<td>Southshire</td>
<td>Womens</td>
<td>.27391</td>
</tr>
<tr>
<td><b>1129</b></td>
<td>Norn Iron Maidens</td>
<td>Belfast</td>
<td>Womens</td>
<td>.27381</td>
</tr>
<tr>
<td><b>1130</b></td>
<td>Hervey Bay Rollerz</td>
<td>Hervey Bay</td>
<td>Womens</td>
<td>.27378</td>
</tr>
<tr>
<td><b>1131</b></td>
<td>River Valley Rollergirls (AR)</td>
<td>Arkansas River Valley</td>
<td>Womens</td>
<td>.27361</td>
</tr>
<tr>
<td><b>1132</b></td>
<td>West Kentucky Rockin' Rollers</td>
<td>West KY</td>
<td>Womens</td>
<td>.27333</td>
</tr>
<tr>
<td><b>1133</b></td>
<td>East Vic Roller Derby</td>
<td>East Vic</td>
<td>Womens</td>
<td>.27317</td>
</tr>
<tr>
<td><b>1134</b></td>
<td>GVA Roller Derby Girls</td>
<td>Geneva</td>
<td>Womens</td>
<td>.27265</td>
</tr>
<tr>
<td><b>1135</b></td>
<td>Roller Derby Luzern</td>
<td>Luzern</td>
<td>Womens</td>
<td>.27242</td>
</tr>
<tr>
<td><b>1136</b></td>
<td>Cajun Rollergirls</td>
<td>Cajun Rollergirls</td>
<td>Womens</td>
<td>.27199</td>
</tr>
<tr>
<td><b>1137</b></td>
<td>WayWARDs</td>
<td>Western Australia</td>
<td>Womens</td>
<td>.27193</td>
</tr>
<tr>
<td><b>1138</b></td>
<td>Roller Derby 72</td>
<td>Le Mans</td>
<td>Womens</td>
<td>.27161</td>
</tr>
<tr>
<td><b>1139</b></td>
<td>Margaret River Roller Derby</td>
<td>Margaret River</td>
<td>Womens</td>
<td>.27145</td>
</tr>
<tr>
<td><b>1140</b></td>
<td>La Bande à ta Mère</td>
<td>Lyonnaises</td>
<td>Womens</td>
<td>.27022</td>
</tr>
<tr>
<td><b>1141</b></td>
<td>ThunderDoms</td>
<td>Dom City</td>
<td>Womens</td>
<td>.26892</td>
</tr>
<tr>
<td><b>1142</b></td>
<td>Las Palmas Roller Derby</td>
<td>Las Palmas</td>
<td>Womens</td>
<td>.26799</td>
</tr>
<tr>
<td><b>1143</b></td>
<td>Roller Derby Ísland</td>
<td>Iceland</td>
<td>Womens</td>
<td>.26785</td>
</tr>
<tr>
<td><b>1144</b></td>
<td>Roller Derby Salamanca</td>
<td>Salamanca</td>
<td>Womens</td>
<td>.26773</td>
</tr>
<tr>
<td><b>1145</b></td>
<td>Coffs Coast Derby Dolls</td>
<td>Coffs Coast</td>
<td>Womens</td>
<td>.26744</td>
</tr>
<tr>
<td><b>1146</b></td>
<td>Deadly Viper Assassination Squad</td>
<td>Toronto</td>
<td>Womens</td>
<td>.26666</td>
</tr>
<tr>
<td><b>1147</b></td>
<td>Northern Beaches Roller Girls</td>
<td>Northern Beaches</td>
<td>Womens</td>
<td>.26583</td>
</tr>
<tr>
<td><b>1148</b></td>
<td>Bilbo Roller Derby</td>
<td>Bilbo</td>
<td>Womens</td>
<td>.26439</td>
</tr>
<tr>
<td><b>1149</b></td>
<td>Les Succubes Roller Derby</td>
<td>Les Succubes</td>
<td>Womens</td>
<td>.26421</td>
</tr>
<tr>
<td><b>1150</b></td>
<td>Riverdale Rollers</td>
<td>Riverdale</td>
<td>Womens</td>
<td>.26415</td>
</tr>
<tr>
<td><b>1151</b></td>
<td>Druid City Dames</td>
<td>Druid City</td>
<td>Womens</td>
<td>.26401</td>
</tr>
<tr>
<td><b>1152</b></td>
<td>The Auver'Niaks</td>
<td>Auver'Niaks</td>
<td>Womens</td>
<td>.26281</td>
</tr>
<tr>
<td><b>1153</b></td>
<td>Dead Ringers</td>
<td>Twin City</td>
<td>Womens</td>
<td>.26278</td>
</tr>
<tr>
<td><b>1154</b></td>
<td>Kassel Roller Derby</td>
<td>Kassel</td>
<td>Womens</td>
<td>.26214</td>
</tr>
<tr>
<td><b>1155</b></td>
<td>UnBreakaBellas</td>
<td>Cologne</td>
<td>Womens</td>
<td>.26199</td>
</tr>
<tr>
<td><b>1156</b></td>
<td>Kill Squad</td>
<td>Killamazoo</td>
<td>Womens</td>
<td>.26186</td>
</tr>
<tr>
<td><b>1157</b></td>
<td>Bedfordshire Rollergirls</td>
<td>Bedfordshire</td>
<td>Womens</td>
<td>.26176</td>
</tr>
<tr>
<td><b>1158</b></td>
<td>Rock 'n' Roller Derby Murcia</td>
<td>Rock 'n' Roller Derby Murcia</td>
<td>Womens</td>
<td>.26108</td>
</tr>
<tr>
<td><b>1159</b></td>
<td>Ace Invaders</td>
<td>Coastal Assassins</td>
<td>Womens</td>
<td>.26098</td>
</tr>
<tr>
<td><b>1160</b></td>
<td>Barbed Wire Betties</td>
<td>Barbed Wire Betties</td>
<td>Womens</td>
<td>.26045</td>
</tr>
<tr>
<td><b>1161</b></td>
<td>Meatgrinders Bremen</td>
<td>Bremen</td>
<td>Womens</td>
<td>.26022</td>
</tr>
<tr>
<td><b>1162</b></td>
<td>East Coast Cyclones</td>
<td>East Coast</td>
<td>Womens</td>
<td>.25982</td>
</tr>
<tr>
<td><b>1163</b></td>
<td>Hawkesbury/Hills Area Roller Derby</td>
<td>Hawkesbury/Hills Area</td>
<td>Womens</td>
<td>.25905</td>
</tr>
<tr>
<td><b>1164</b></td>
<td>Bone City Rollers</td>
<td>Bone City</td>
<td>Womens</td>
<td>.25899</td>
</tr>
<tr>
<td><b>1165</b></td>
<td>Badass Beavers</td>
<td>Gothenburg</td>
<td>Womens</td>
<td>.25813</td>
</tr>
<tr>
<td><b>1166</b></td>
<td>Deathrow Hull</td>
<td>Deathrow</td>
<td>Womens</td>
<td>.25810</td>
</tr>
<tr>
<td><b>1167</b></td>
<td>Roller Derby des Nordiks de Touraine</td>
<td>Tours</td>
<td>Womens</td>
<td>.25728</td>
</tr>
<tr>
<td><b>1168</b></td>
<td>Whenua Fatales Roller Derby League</td>
<td>Whenua Fatales</td>
<td>Womens</td>
<td>.25678</td>
</tr>
<tr>
<td><b>1169</b></td>
<td>Pittsburgh East Roller Villains (Women's)</td>
<td>Pittsburgh East (W)</td>
<td>Womens</td>
<td>.25611</td>
</tr>
<tr>
<td><b>1170</b></td>
<td>Sucker Punch Roller Derby</td>
<td>Nürnberg</td>
<td>Womens</td>
<td>.25576</td>
</tr>
<tr>
<td><b>1171</b></td>
<td>All City Rollers</td>
<td>All City</td>
<td>Womens</td>
<td>.25531</td>
</tr>
<tr>
<td><b>1172</b></td>
<td>Canadian Clubbers</td>
<td>Border City Brawlers</td>
<td>Womens</td>
<td>.25506</td>
</tr>
<tr>
<td><b>1173</b></td>
<td>Uppsala Roller Derby</td>
<td>Uppsala</td>
<td>Womens</td>
<td>.25482</td>
</tr>
<tr>
<td><b>1174</b></td>
<td>Brutal Belles</td>
<td>Cedar Rapids Rollergirls</td>
<td>Womens</td>
<td>.25452</td>
</tr>
<tr>
<td><b>1175</b></td>
<td>Skagit Valley Roller Derby</td>
<td>Skagit Valley</td>
<td>Womens</td>
<td>.25402</td>
</tr>
<tr>
<td><b>1176</b></td>
<td>The Dire Skates</td>
<td>Dire Skates</td>
<td>Womens</td>
<td>.25383</td>
</tr>
<tr>
<td><b>1177</b></td>
<td>Galway City She Devils</td>
<td>Galway</td>
<td>Womens</td>
<td>.25362</td>
</tr>
<tr>
<td><b>1178</b></td>
<td>Psyko'Quads SGS Roller Derby</td>
<td>Psyko'Quads</td>
<td>Womens</td>
<td>.25339</td>
</tr>
<tr>
<td><b>1179</b></td>
<td>Orcet Roller Derby (Team B)</td>
<td>Orcet (Womens)</td>
<td>Womens</td>
<td>.25234</td>
</tr>
<tr>
<td><b>1180</b></td>
<td>Revolution Roller Derby</td>
<td>Rolling Valkyries</td>
<td>Womens</td>
<td>.25218</td>
</tr>
<tr>
<td><b>1181</b></td>
<td>Rimini Roller Derby</td>
<td>Stray Beez</td>
<td>Womens</td>
<td>.25206</td>
</tr>
<tr>
<td><b>1182</b></td>
<td>The Night Terrors</td>
<td>RGA The Wreckoning</td>
<td>Womens</td>
<td>.25204</td>
</tr>
<tr>
<td><b>1183</b></td>
<td>Limoges Roller Skating</td>
<td>Limoges</td>
<td>Womens</td>
<td>.25198</td>
</tr>
<tr>
<td><b>1184</b></td>
<td>HARD B</td>
<td>Hulls Angels</td>
<td>Womens</td>
<td>.25161</td>
</tr>
<tr>
<td><b>1185</b></td>
<td>Broadbarians</td>
<td>East Lansing</td>
<td>Womens</td>
<td>.25043</td>
</tr>
<tr>
<td><b>1186</b></td>
<td>Chemical Valley Rollergirls</td>
<td>Chemical Valley</td>
<td>Womens</td>
<td>.25022</td>
</tr>
<tr>
<td><b>1187</b></td>
<td>Municorns</td>
<td>Munich</td>
<td>Womens</td>
<td>.25002</td>
</tr>
<tr>
<td><b>1188</b></td>
<td>Sin City Rollers</td>
<td>Sin City Rollers</td>
<td>Womens</td>
<td>.24829</td>
</tr>
<tr>
<td><b>1189</b></td>
<td>Northshore Roller Derby</td>
<td>Northshore</td>
<td>Womens</td>
<td>.24828</td>
</tr>
<tr>
<td><b>1190</b></td>
<td>Ketchikan Rain Forest Roller Girls</td>
<td>Ketchikan</td>
<td>Womens</td>
<td>.24804</td>
</tr>
<tr>
<td><b>1191</b></td>
<td>Waterford City Viqueens</td>
<td>Waterford</td>
<td>Womens</td>
<td>.24704</td>
</tr>
<tr>
<td><b>1192</b></td>
<td>Motor City Madames</td>
<td>Durham (Canada)</td>
<td>Womens</td>
<td>.24627</td>
</tr>
<tr>
<td><b>1193</b></td>
<td>Les Passeuses Dâmes</td>
<td>Les Passeuses Dâmes</td>
<td>Womens</td>
<td>.24606</td>
</tr>
<tr>
<td><b>1194</b></td>
<td>Shitty Village B-Pol</td>
<td>Oulu</td>
<td>Womens</td>
<td>.24562</td>
</tr>
<tr>
<td><b>1195</b></td>
<td>Anjou Derby Girls</td>
<td>Anjou</td>
<td>Womens</td>
<td>.24440</td>
</tr>
<tr>
<td><b>1196</b></td>
<td>Demolition Dolls Roller Derby</td>
<td>Cookeville</td>
<td>Womens</td>
<td>.24388</td>
</tr>
<tr>
<td><b>1197</b></td>
<td>Kokomo City of Fists Roller Derby</td>
<td>Kokomo</td>
<td>Womens</td>
<td>.24341</td>
</tr>
<tr>
<td><b>1198</b></td>
<td>Beat City Bedrockers</td>
<td>Hartford Area</td>
<td>Womens</td>
<td>.24305</td>
</tr>
<tr>
<td><b>1199</b></td>
<td>New Town Roller Girls</td>
<td>New Town</td>
<td>Womens</td>
<td>.24285</td>
</tr>
<tr>
<td><b>1200</b></td>
<td>Roll-On Derby</td>
<td>Roll-On</td>
<td>Womens</td>
<td>.24164</td>
</tr>
<tr>
<td><b>1201</b></td>
<td>Orleans Roller Derby Team B</td>
<td>Orléans</td>
<td>Womens</td>
<td>.24096</td>
</tr>
<tr>
<td><b>1202</b></td>
<td>Dirty Jersey Roller Derby</td>
<td>Dirty Jersey</td>
<td>Womens</td>
<td>.24026</td>
</tr>
<tr>
<td><b>1203</b></td>
<td>Roller Derby Chambéry</td>
<td>Chambéry</td>
<td>Womens</td>
<td>.24011</td>
</tr>
<tr>
<td><b>1204</b></td>
<td>Roller Derby A Coruña</td>
<td>A Coruña</td>
<td>Womens</td>
<td>.23970</td>
</tr>
<tr>
<td><b>1205</b></td>
<td>Pair O' Dice City Rollers</td>
<td>Pair O' Dice</td>
<td>Womens</td>
<td>.23953</td>
</tr>
<tr>
<td><b>1206</b></td>
<td>Les Petites Frappes</td>
<td>Lutece</td>
<td>Womens</td>
<td>.23834</td>
</tr>
<tr>
<td><b>1207</b></td>
<td>Hostess City Hellions</td>
<td>Savannah</td>
<td>Womens</td>
<td>.23819</td>
</tr>
<tr>
<td><b>1208</b></td>
<td>East Coast Derby Dolls</td>
<td>East Coast</td>
<td>Womens</td>
<td>.23780</td>
</tr>
<tr>
<td><b>1209</b></td>
<td>Maniac Monsters Mainz</td>
<td>Maniac Monsters Mainz</td>
<td>Womens</td>
<td>.23607</td>
</tr>
<tr>
<td><b>1210</b></td>
<td>Demolitia Derby Queens</td>
<td>Demolitia</td>
<td>Womens</td>
<td>.23559</td>
</tr>
<tr>
<td><b>1211</b></td>
<td>Northumberland Roller Girls</td>
<td>Northumberland</td>
<td>Womens</td>
<td>.23542</td>
</tr>
<tr>
<td><b>1212</b></td>
<td>Bridgend Roller Derby</td>
<td>Bridgend</td>
<td>Womens</td>
<td>.23537</td>
</tr>
<tr>
<td><b>1213</b></td>
<td>Mid-Hudson Misfits</td>
<td>Mid-Hudson</td>
<td>Womens</td>
<td>.23501</td>
</tr>
<tr>
<td><b>1214</b></td>
<td>Southern Belles Roller Derby</td>
<td>Southern Belles</td>
<td>Womens</td>
<td>.23410</td>
</tr>
<tr>
<td><b>1215</b></td>
<td>North Pole</td>
<td>North Pole</td>
<td>Womens</td>
<td>.23261</td>
</tr>
<tr>
<td><b>1216</b></td>
<td>Team Regional Victoria</td>
<td>Rolling Matildas</td>
<td>Womens</td>
<td>.23260</td>
</tr>
<tr>
<td><b>1217</b></td>
<td>Atlantic Breakers B</td>
<td>Cornwall</td>
<td>Womens</td>
<td>.23240</td>
</tr>
<tr>
<td><b>1218</b></td>
<td>Cape Girardeau Roller Derby</td>
<td>Cape Girardeau</td>
<td>Womens</td>
<td>.23152</td>
</tr>
<tr>
<td><b>1219</b></td>
<td>Roller Derby Mâcon (Women's)</td>
<td>Bananas Clit</td>
<td>Womens</td>
<td>.23030</td>
</tr>
<tr>
<td><b>1220</b></td>
<td>Peterborough Area Roller Dervy</td>
<td>PARDy</td>
<td>Womens</td>
<td>.23005</td>
</tr>
<tr>
<td><b>1221</b></td>
<td>Hell's Orchard Roller Derby</td>
<td>First Settlement</td>
<td>Womens</td>
<td>.22966</td>
</tr>
<tr>
<td><b>1222</b></td>
<td>The Team B'East</td>
<td>Strasbourg</td>
<td>Womens</td>
<td>.22918</td>
</tr>
<tr>
<td><b>1223</b></td>
<td>Les Faucheuses</td>
<td>Rouen</td>
<td>Womens</td>
<td>.22641</td>
</tr>
<tr>
<td><b>1224</b></td>
<td>Valley Valkyries</td>
<td>Tweed Valley</td>
<td>Womens</td>
<td>.22597</td>
</tr>
<tr>
<td><b>1225</b></td>
<td>Dockyard Brawlers</td>
<td>Halifax</td>
<td>Womens</td>
<td>.22592</td>
</tr>
<tr>
<td><b>1226</b></td>
<td>Roller Derby Besançon</td>
<td>Besançon</td>
<td>Womens</td>
<td>.22543</td>
</tr>
<tr>
<td><b>1227</b></td>
<td>Cape Breton Roller Derby</td>
<td>Cape Breton</td>
<td>Womens</td>
<td>.22475</td>
</tr>
<tr>
<td><b>1228</b></td>
<td>The Disloyalists</td>
<td>Kingston</td>
<td>Womens</td>
<td>.22299</td>
</tr>
<tr>
<td><b>1229</b></td>
<td>Mac-Town Sugar Skulls</td>
<td>Mac-Town</td>
<td>Womens</td>
<td>.22175</td>
</tr>
<tr>
<td><b>1230</b></td>
<td>Roller Derby Argenteuil</td>
<td>Argenteuil</td>
<td>Womens</td>
<td>.22027</td>
</tr>
<tr>
<td><b>1231</b></td>
<td>CORD B Squad</td>
<td>Central Ohio</td>
<td>Womens</td>
<td>.21854</td>
</tr>
<tr>
<td><b>1232</b></td>
<td>Prague City Roller Derby B</td>
<td>Prague</td>
<td>Womens</td>
<td>.21665</td>
</tr>
<tr>
<td><b>1233</b></td>
<td>Belfast City Rockets</td>
<td>Belfast City</td>
<td>Womens</td>
<td>.21651</td>
</tr>
<tr>
<td><b>1234</b></td>
<td>North Devon Roller Girls B Team</td>
<td>North Devon</td>
<td>Womens</td>
<td>.21624</td>
</tr>
<tr>
<td><b>1235</b></td>
<td>Northern Ontario Roller Derby</td>
<td>NORD Men's</td>
<td>Mens</td>
<td>.21519</td>
</tr>
<tr>
<td><b>1236</b></td>
<td>North West Roller Derby</td>
<td>North West</td>
<td>Womens</td>
<td>.21476</td>
</tr>
<tr>
<td><b>1237</b></td>
<td>Seinäjoki Roller Derby</td>
<td>Seinäjoki</td>
<td>Womens</td>
<td>.21200</td>
</tr>
<tr>
<td><b>1238</b></td>
<td>Roller Derby Le Havre</td>
<td>Le Havre</td>
<td>Womens</td>
<td>.21111</td>
</tr>
<tr>
<td><b>1239</b></td>
<td>Wharf City Rollers</td>
<td>Wharf City</td>
<td>Womens</td>
<td>.20974</td>
</tr>
<tr>
<td><b>1240</b></td>
<td>Örebro Roller Derby</td>
<td>Örebro</td>
<td>Womens</td>
<td>.20854</td>
</tr>
<tr>
<td><b>1241</b></td>
<td>Oslo Tiger City Beasts</td>
<td>Oslo</td>
<td>Womens</td>
<td>.20628</td>
</tr>
<tr>
<td><b>1242</b></td>
<td>Easo Avengers Roller Derby</td>
<td>Easo Avengers</td>
<td>Womens</td>
<td>.20559</td>
</tr>
<tr>
<td><b>1243</b></td>
<td>American Revolution Roller Derby</td>
<td>American Revolution</td>
<td>Womens</td>
<td>.20467</td>
</tr>
<tr>
<td><b>1244</b></td>
<td>Bonebreakers Bern</td>
<td>Bern</td>
<td>Womens</td>
<td>.20456</td>
</tr>
<tr>
<td><b>1245</b></td>
<td>Dollinquents</td>
<td>Capital City</td>
<td>Womens</td>
<td>.20409</td>
</tr>
<tr>
<td><b>1246</b></td>
<td>Eerie Roller Girls</td>
<td>Eerie Roller Girls</td>
<td>Womens</td>
<td>.20392</td>
</tr>
<tr>
<td><b>1247</b></td>
<td>Tours B team</td>
<td>Tours</td>
<td>Womens</td>
<td>.20383</td>
</tr>
<tr>
<td><b>1248</b></td>
<td>Swan City Derby Dames</td>
<td>Swan City</td>
<td>Womens</td>
<td>.20229</td>
</tr>
<tr>
<td><b>1249</b></td>
<td>Gold City Rollers</td>
<td>Gold City</td>
<td>Womens</td>
<td>.20221</td>
</tr>
<tr>
<td><b>1250</b></td>
<td>Eastside Derby Girls</td>
<td>Eastside Derby</td>
<td>Womens</td>
<td>.20221</td>
</tr>
<tr>
<td><b>1251</b></td>
<td>Blackland Rockin' K-Rollers</td>
<td>Blackland</td>
<td>Womens</td>
<td>.20204</td>
</tr>
<tr>
<td><b>1252</b></td>
<td>REC League - Nantes</td>
<td>Nantes</td>
<td>Womens</td>
<td>.20134</td>
</tr>
<tr>
<td><b>1253</b></td>
<td>Roller Derby Vigo</td>
<td>RDV</td>
<td>Womens</td>
<td>.20118</td>
</tr>
<tr>
<td><b>1254</b></td>
<td>Mobile's Derby Darlings</td>
<td>Mobile</td>
<td>Womens</td>
<td>.19959</td>
</tr>
<tr>
<td><b>1255</b></td>
<td>Little Steel Derby Girls</td>
<td>Little Steel Derby Girls</td>
<td>Womens</td>
<td>.19927</td>
</tr>
<tr>
<td><b>1256</b></td>
<td>WestCo Derby</td>
<td>WestCo</td>
<td>Womens</td>
<td>.19923</td>
</tr>
<tr>
<td><b>1257</b></td>
<td>Mortal Condate</td>
<td>Rennes</td>
<td>Womens</td>
<td>.19912</td>
</tr>
<tr>
<td><b>1258</b></td>
<td>J-Town Roller Girls</td>
<td>Flood City Sirens</td>
<td>Womens</td>
<td>.19802</td>
</tr>
<tr>
<td><b>1259</b></td>
<td>Norfolk County Roller Derby</td>
<td>Norfolk County</td>
<td>Womens</td>
<td>.19457</td>
</tr>
<tr>
<td><b>1260</b></td>
<td>Albany Roller Derby League</td>
<td>Albany Roller Derby</td>
<td>Womens</td>
<td>.19296</td>
</tr>
<tr>
<td><b>1261</b></td>
<td>Pink Peril Rollerderby</td>
<td>Pink Peril</td>
<td>Womens</td>
<td>.19204</td>
</tr>
<tr>
<td><b>1262</b></td>
<td>Roller Derby Luxembourg</td>
<td>Luxembourg</td>
<td>Womens</td>
<td>.19076</td>
</tr>
<tr>
<td><b>1263</b></td>
<td>Coventry Roller Derby</td>
<td>Coventry</td>
<td>Womens</td>
<td>.19020</td>
</tr>
<tr>
<td><b>1264</b></td>
<td>The Royal Brigade</td>
<td>The Royal Army</td>
<td>Womens</td>
<td>.18800</td>
</tr>
<tr>
<td><b>1265</b></td>
<td>Derailers</td>
<td>South Shore</td>
<td>Womens</td>
<td>.18754</td>
</tr>
<tr>
<td><b>1266</b></td>
<td>Outrage</td>
<td>DuPage Derby</td>
<td>Womens</td>
<td>.18506</td>
</tr>
<tr>
<td><b>1267</b></td>
<td>B Devils</td>
<td>Penn Jersey</td>
<td>Womens</td>
<td>.18429</td>
</tr>
<tr>
<td><b>1268</b></td>
<td>Berlin Rollergirls</td>
<td>Berlin Rollergirls</td>
<td>Womens</td>
<td>.18354</td>
</tr>
<tr>
<td><b>1269</b></td>
<td>Roe City Rollers</td>
<td>Roe City Rollers</td>
<td>Womens</td>
<td>.18315</td>
</tr>
<tr>
<td><b>1270</b></td>
<td>Kapiti Coast Derby Collective</td>
<td>Kapiti Coast</td>
<td>Womens</td>
<td>.18072</td>
</tr>
<tr>
<td><b>1271</b></td>
<td>Appalachian Iron Maidens</td>
<td>Appalachian Iron Maidens</td>
<td>Womens</td>
<td>.17901</td>
</tr>
<tr>
<td><b>1272</b></td>
<td>Montgomery Roller Derby</td>
<td>Montgomery</td>
<td>Womens</td>
<td>.17777</td>
</tr>
<tr>
<td><b>1273</b></td>
<td>Poison Apples Roller Derby</td>
<td>Poison Apples</td>
<td>Womens</td>
<td>.17525</td>
</tr>
<tr>
<td><b>1274</b></td>
<td>Roller Derby Bretenoux Biars</td>
<td>Enragées</td>
<td>Womens</td>
<td>.16623</td>
</tr>
<tr>
<td><b>1275</b></td>
<td>Karlstad Roller Derby</td>
<td>Karlstad</td>
<td>Womens</td>
<td>.15813</td>
</tr>
<tr>
<td><b>1276</b></td>
<td>Valley of the Derby Dollinquents</td>
<td>Voodoo Dolls</td>
<td>Womens</td>
<td>.15160</td>
</tr>
<tr>
<td><b>1277</b></td>
<td>Rocket Dolls Roller Derby Coimbra</td>
<td>Coimbra</td>
<td>Womens</td>
<td>.14728</td>
</tr>
<tr>
<td><b>1278</b></td>
<td>BURDs</td>
<td>Uppsala</td>
<td>Womens</td>
<td>.13909</td>
</tr>
<tr>
<td><b>1279</b></td>
<td>Roller Derby Palois</td>
<td>Pau</td>
<td>Womens</td>
<td>.13151</td>
</tr>
<tr>
<td><b>1280</b></td>
<td>Roller Derby Rochefort</td>
<td>Rochefort</td>
<td>Womens</td>
<td>.12658</td>
</tr>
<tr>
<td><b>1281</b></td>
<td>Wasa Roller Derby</td>
<td>Wasa</td>
<td>Womens</td>
<td>.12636</td>
</tr>
<tr>
<td><b>1282</b></td>
<td>Rail City Rollers</td>
<td>Rail City</td>
<td>Womens</td>
<td>.12436</td>
</tr>
<tr>
<td><b>1283</b></td>
<td>Rockabellas Roller Derby League</td>
<td>Rockabellas</td>
<td>Womens</td>
<td>.10354</td>
</tr>
<tr>
<td><b>1284</b></td>
<td>Southern Harm Derby Dames</td>
<td>Southern Harm</td>
<td>Womens</td>
<td>.09721</td>
</tr>
<tr>
<td><b>1285</b></td>
<td>Pori Rolling Brigade</td>
<td>Pori</td>
<td>Womens</td>
<td>.09234</td>
</tr>
<tr>
<td><b>1286</b></td>
<td>Reynoldsville Rebel Rollers</td>
<td>Reynoldsville</td>
<td>Womens</td>
<td>.08957</td>
</tr>
<tr>
<td><b>1287</b></td>
<td>Lisbon Grrrls Roller Derby</td>
<td>Lisbon</td>
<td>Womens</td>
<td>.04746</td>
</tr>
<tr>
<td><b>1288</b></td>
<td>Silver Bridge Bruisers</td>
<td>Silver Bridge</td>
<td>Womens</td>
<td>.01293</td>
</tr>
</tbody>
</table>
<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/4/">NEXT PAGE

</a></strong>** Yes, this is an error in the FTS dataset.

<!--nextpage-->

We've also broken this up into Women's and Men's Rankings, shown below: [<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/5/">CLICK HERE TO SKIP TO MEN</a></strong>] [<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/3/">CLICK HERE TO SKIP UP TO TOP OF FULL RANKING</a></strong>]
<h2>Women's Derby International Rankings 1 October 2016</h2>
<table>
<tbody>
<tr>
<td>RANK</td>
<td>Global Rank</td>
<td>TEAM</td>
<td>League</td>
<td>Type</td>
<td>Rating</td>
</tr>
<tr>
<td><b>1</b></td>
<td>1</td>
<td>Gotham Girls Roller Derby</td>
<td>Gotham</td>
<td>Womens</td>
<td>1.00000</td>
</tr>
<tr>
<td><b>2</b></td>
<td>2</td>
<td>Victorian Roller Derby League</td>
<td>Victoria</td>
<td>Womens</td>
<td>.96938</td>
</tr>
<tr>
<td><b>3</b></td>
<td>4</td>
<td>Angel City Derby Girls</td>
<td>Angel City</td>
<td>Womens</td>
<td>.95143</td>
</tr>
<tr>
<td><b>4</b></td>
<td>5</td>
<td>London Rollergirls</td>
<td>London</td>
<td>Womens</td>
<td>.93049</td>
</tr>
<tr>
<td><b>5</b></td>
<td>6</td>
<td>Rose City Rollers</td>
<td>Rose</td>
<td>Womens</td>
<td>.92153</td>
</tr>
<tr>
<td><b>6</b></td>
<td>7</td>
<td>Texas Rollergirls</td>
<td>Texas</td>
<td>Womens</td>
<td>.91309</td>
</tr>
<tr>
<td><b>7</b></td>
<td>12</td>
<td>Denver Roller Derby</td>
<td>Denver</td>
<td>Womens</td>
<td>.86656</td>
</tr>
<tr>
<td><b>8</b></td>
<td>13</td>
<td>Minnesota RollerGirls</td>
<td>Minnesota</td>
<td>Womens</td>
<td>.85927</td>
</tr>
<tr>
<td><b>9</b></td>
<td>15</td>
<td>Arch Rival Roller Derby</td>
<td>Arch Rival</td>
<td>Womens</td>
<td>.85231</td>
</tr>
<tr>
<td><b>10</b></td>
<td>16</td>
<td>Jacksonville Roller Girls</td>
<td>Jacksonville</td>
<td>Womens</td>
<td>.85043</td>
</tr>
<tr>
<td><b>11</b></td>
<td>17</td>
<td>Atlanta Rollergirls</td>
<td>Atlanta</td>
<td>Womens</td>
<td>.84234</td>
</tr>
<tr>
<td><b>12</b></td>
<td>18</td>
<td>Rat City Roller Girls</td>
<td>Rat City</td>
<td>Womens</td>
<td>.83912</td>
</tr>
<tr>
<td><b>13</b></td>
<td>19</td>
<td>Tampa Roller Derby</td>
<td>Tampa</td>
<td>Womens</td>
<td>.82738</td>
</tr>
<tr>
<td><b>14</b></td>
<td>20</td>
<td>Crime City Rollers</td>
<td>Crime City</td>
<td>Womens</td>
<td>.82178</td>
</tr>
<tr>
<td><b>15</b></td>
<td>23</td>
<td>Dallas Derby Devils</td>
<td>Dallas</td>
<td>Womens</td>
<td>.81959</td>
</tr>
<tr>
<td><b>16</b></td>
<td>24</td>
<td>Philly Roller Derby</td>
<td>Philly</td>
<td>Womens</td>
<td>.81896</td>
</tr>
<tr>
<td><b>17</b></td>
<td>25</td>
<td>Montreal Roller Derby</td>
<td>Montreal</td>
<td>Womens</td>
<td>.81175</td>
</tr>
<tr>
<td><b>18</b></td>
<td>26</td>
<td>Bay Area Derby</td>
<td>Bay Area</td>
<td>Womens</td>
<td>.80578</td>
</tr>
<tr>
<td><b>19</b></td>
<td>27</td>
<td>Terminal City Rollergirls</td>
<td>Terminal City</td>
<td>Womens</td>
<td>.79932</td>
</tr>
<tr>
<td><b>20</b></td>
<td>28</td>
<td>Team United Roller Derby</td>
<td>Team United</td>
<td>Womens</td>
<td>.79920</td>
</tr>
<tr>
<td><b>21</b></td>
<td>29</td>
<td>Detroit Derby Girls</td>
<td>Detroit</td>
<td>Womens</td>
<td>.79105</td>
</tr>
<tr>
<td><b>22</b></td>
<td>31</td>
<td>Rainy City Roller Derby</td>
<td>Rainy City (UK)</td>
<td>Womens</td>
<td>.78558</td>
</tr>
<tr>
<td><b>23</b></td>
<td>35</td>
<td>Team Gold</td>
<td>Bay Area</td>
<td>Womens</td>
<td>.77162</td>
</tr>
<tr>
<td><b>24</b></td>
<td>36</td>
<td>Helsinki Roller Derby</td>
<td>Helsinki</td>
<td>Womens</td>
<td>.76742</td>
</tr>
<tr>
<td><b>25</b></td>
<td>37</td>
<td>Stockholm Roller Derby</td>
<td>Stockholm</td>
<td>Womens</td>
<td>.76490</td>
</tr>
<tr>
<td><b>26</b></td>
<td>38</td>
<td>Boston Roller Derby</td>
<td>Boston</td>
<td>Womens</td>
<td>.75800</td>
</tr>
<tr>
<td><b>27</b></td>
<td>39</td>
<td>Queen Bees</td>
<td>Victoria</td>
<td>Womens</td>
<td>.75495</td>
</tr>
<tr>
<td><b>28</b></td>
<td>40</td>
<td>Kallio Rolling Rainbow</td>
<td>Kallio</td>
<td>Womens</td>
<td>.75377</td>
</tr>
<tr>
<td><b>29</b></td>
<td>42</td>
<td>Sun State Roller Girls</td>
<td>Sun State</td>
<td>Womens</td>
<td>.75199</td>
</tr>
<tr>
<td><b>30</b></td>
<td>45</td>
<td>Kinapori Fistfunkers</td>
<td>Kallio</td>
<td>Womens</td>
<td>.74133</td>
</tr>
<tr>
<td><b>31</b></td>
<td>46</td>
<td>Rocky Mountain Rollergirls</td>
<td>Rocky Mtn.</td>
<td>Womens</td>
<td>.74095</td>
</tr>
<tr>
<td><b>32</b></td>
<td>47</td>
<td>Dow Jones Average</td>
<td>Shock Exchange</td>
<td>Womens**</td>
<td>.73985</td>
</tr>
<tr>
<td><b>33</b></td>
<td>48</td>
<td>Santa Cruz Derby Girls</td>
<td>Santa Cruz</td>
<td>Womens</td>
<td>.73756</td>
</tr>
<tr>
<td><b>34</b></td>
<td>49</td>
<td>Roller Derby Toulouse (Women's)</td>
<td>Toulouse</td>
<td>Womens</td>
<td>.73601</td>
</tr>
<tr>
<td><b>35</b></td>
<td>50</td>
<td>Middlesbrough Milk Rollers</td>
<td>Middlesbrough</td>
<td>Womens</td>
<td>.73592</td>
</tr>
<tr>
<td><b>36</b></td>
<td>51</td>
<td>Bruising Altitude</td>
<td>Denver</td>
<td>Womens</td>
<td>.73527</td>
</tr>
<tr>
<td><b>37</b></td>
<td>52</td>
<td>Paris Rollergirls</td>
<td>Paris</td>
<td>Womens</td>
<td>.73371</td>
</tr>
<tr>
<td><b>38</b></td>
<td>53</td>
<td>Columbia QuadSquad Rollergirls</td>
<td>Columbia</td>
<td>Womens</td>
<td>.73112</td>
</tr>
<tr>
<td><b>39</b></td>
<td>54</td>
<td>Queen City Roller Girls</td>
<td>Queen City</td>
<td>Womens</td>
<td>.73006</td>
</tr>
<tr>
<td><b>40</b></td>
<td>56</td>
<td>Arizona Roller Derby</td>
<td>Arizona</td>
<td>Womens</td>
<td>.72557</td>
</tr>
<tr>
<td><b>41</b></td>
<td>57</td>
<td>Sydney Roller Derby League</td>
<td>Sydney Assassins</td>
<td>Womens</td>
<td>.72393</td>
</tr>
<tr>
<td><b>42</b></td>
<td>58</td>
<td>Ohio Roller Derby</td>
<td>Ohio</td>
<td>Womens</td>
<td>.72335</td>
</tr>
<tr>
<td><b>43</b></td>
<td>60</td>
<td>Steel City Roller Derby</td>
<td>Steel City</td>
<td>Womens</td>
<td>.72119</td>
</tr>
<tr>
<td><b>44</b></td>
<td>61</td>
<td>Wall Street Traitors</td>
<td>Gotham</td>
<td>Womens</td>
<td>.72090</td>
</tr>
<tr>
<td><b>45</b></td>
<td>62</td>
<td>Firing Squad (TX)</td>
<td>Texas</td>
<td>Womens</td>
<td>.72011</td>
</tr>
<tr>
<td><b>46</b></td>
<td>63</td>
<td>No Coast Derby Girls</td>
<td>No Coast</td>
<td>Womens</td>
<td>.71938</td>
</tr>
<tr>
<td><b>47</b></td>
<td>64</td>
<td>Charm City Roller Girls</td>
<td>Charm City</td>
<td>Womens</td>
<td>.71668</td>
</tr>
<tr>
<td><b>48</b></td>
<td>66</td>
<td>Mad Rollin' Dolls Roller Derby</td>
<td>Madison</td>
<td>Womens</td>
<td>.71483</td>
</tr>
<tr>
<td><b>49</b></td>
<td>68</td>
<td>Axles of Annihilation</td>
<td>Rose</td>
<td>Womens</td>
<td>.71055</td>
</tr>
<tr>
<td><b>50</b></td>
<td>69</td>
<td>Windy City Rollers</td>
<td>Windy City</td>
<td>Womens</td>
<td>.70990</td>
</tr>
<tr>
<td><b>51</b></td>
<td>70</td>
<td>Perth Roller Derby</td>
<td>Perth</td>
<td>Womens</td>
<td>.70882</td>
</tr>
<tr>
<td><b>52</b></td>
<td>71</td>
<td>Ann Arbor Derby Dimes</td>
<td>Ann Arbor</td>
<td>Womens</td>
<td>.70793</td>
</tr>
<tr>
<td><b>53</b></td>
<td>72</td>
<td>Sacred City Derby Girls</td>
<td>Sacred</td>
<td>Womens</td>
<td>.70728</td>
</tr>
<tr>
<td><b>54</b></td>
<td>73</td>
<td>Lille Roller Girls</td>
<td>Lille</td>
<td>Womens</td>
<td>.70461</td>
</tr>
<tr>
<td><b>55</b></td>
<td>74</td>
<td>Calgary Roller Derby Association</td>
<td>Calgary</td>
<td>Womens</td>
<td>.70148</td>
</tr>
<tr>
<td><b>56</b></td>
<td>75</td>
<td>Brandywine Roller Derby</td>
<td>Brandywine</td>
<td>Womens</td>
<td>.70068</td>
</tr>
<tr>
<td><b>57</b></td>
<td>76</td>
<td>Naptown Roller Girls</td>
<td>Naptown</td>
<td>Womens</td>
<td>.70031</td>
</tr>
<tr>
<td><b>58</b></td>
<td>77</td>
<td>Tucson Roller Derby</td>
<td>Tucson</td>
<td>Womens</td>
<td>.69991</td>
</tr>
<tr>
<td><b>59</b></td>
<td>78</td>
<td>Charlottesville Derby Dames</td>
<td>Charlottesville</td>
<td>Womens</td>
<td>.69811</td>
</tr>
<tr>
<td><b>60</b></td>
<td>79</td>
<td>Orangeville Roller Girls</td>
<td>ORG All-Stars</td>
<td>Womens</td>
<td>.69779</td>
</tr>
<tr>
<td><b>61</b></td>
<td>81</td>
<td>Dock City Rollers</td>
<td>Dock City</td>
<td>Womens</td>
<td>.69598</td>
</tr>
<tr>
<td><b>62</b></td>
<td>82</td>
<td>Blue Ridge Rollergirls</td>
<td>Blue Ridge</td>
<td>Womens</td>
<td>.69433</td>
</tr>
<tr>
<td><b>63</b></td>
<td>83</td>
<td>Wheels of Mayhem</td>
<td>Wheels of Mayhem</td>
<td>Womens</td>
<td>.69425</td>
</tr>
<tr>
<td><b>64</b></td>
<td>84</td>
<td>Houston Roller Derby</td>
<td>Houston</td>
<td>Womens</td>
<td>.69303</td>
</tr>
<tr>
<td><b>65</b></td>
<td>85</td>
<td>Wasatch Roller Derby</td>
<td>Wasatch</td>
<td>Womens</td>
<td>.68927</td>
</tr>
<tr>
<td><b>66</b></td>
<td>86</td>
<td>Tiger Bay Brawlers</td>
<td>Tiger Bay</td>
<td>Womens</td>
<td>.68899</td>
</tr>
<tr>
<td><b>67</b></td>
<td>87</td>
<td>2x4 Roller Derby</td>
<td>2x4</td>
<td>Womens</td>
<td>.68665</td>
</tr>
<tr>
<td><b>68</b></td>
<td>88</td>
<td>Paradise City Roller Derby</td>
<td>Paradise City</td>
<td>Womens</td>
<td>.68649</td>
</tr>
<tr>
<td><b>69</b></td>
<td>90</td>
<td>Canberra Roller Derby League</td>
<td>Canberra</td>
<td>Womens</td>
<td>.68405</td>
</tr>
<tr>
<td><b>70</b></td>
<td>92</td>
<td>Bruise Crew</td>
<td>Tampa</td>
<td>Womens</td>
<td>.67985</td>
</tr>
<tr>
<td><b>71</b></td>
<td>93</td>
<td>London Brawl Saints</td>
<td>London</td>
<td>Womens</td>
<td>.67908</td>
</tr>
<tr>
<td><b>72</b></td>
<td>96</td>
<td>Adelaide Roller Derby</td>
<td>Adeladies</td>
<td>Womens</td>
<td>.67534</td>
</tr>
<tr>
<td><b>73</b></td>
<td>97</td>
<td>Bear City Roller Derby</td>
<td>Bear City</td>
<td>Womens</td>
<td>.67390</td>
</tr>
<tr>
<td><b>74</b></td>
<td>98</td>
<td>Jet City Rollergirls</td>
<td>Jet City</td>
<td>Womens</td>
<td>.67269</td>
</tr>
<tr>
<td><b>75</b></td>
<td>99</td>
<td>Dublin Roller Derby</td>
<td>Dublin</td>
<td>Womens</td>
<td>.67085</td>
</tr>
<tr>
<td><b>76</b></td>
<td>100</td>
<td>Boulder County Bombers</td>
<td>Boulder County</td>
<td>Womens</td>
<td>.66812</td>
</tr>
<tr>
<td><b>77</b></td>
<td>101</td>
<td>Newcastle Roller Girls</td>
<td>Newcastle</td>
<td>Womens</td>
<td>.66733</td>
</tr>
<tr>
<td><b>78</b></td>
<td>102</td>
<td>Rage City Rollergirls</td>
<td>Rage City</td>
<td>Womens</td>
<td>.66601</td>
</tr>
<tr>
<td><b>79</b></td>
<td>103</td>
<td>Rocket Queens</td>
<td>Angel City</td>
<td>Womens</td>
<td>.66594</td>
</tr>
<tr>
<td><b>80</b></td>
<td>104</td>
<td>Nantes Derby Girls</td>
<td>Nantes</td>
<td>Womens</td>
<td>.66511</td>
</tr>
<tr>
<td><b>81</b></td>
<td>105</td>
<td>Nashville Rollergirls</td>
<td>Nashville</td>
<td>Womens</td>
<td>.66389</td>
</tr>
<tr>
<td><b>82</b></td>
<td>106</td>
<td>Tri-City Roller Derby</td>
<td>Tri-City</td>
<td>Womens</td>
<td>.66235</td>
</tr>
<tr>
<td><b>83</b></td>
<td>107</td>
<td>Auld Reekie Roller Girls</td>
<td>Auld Reekie</td>
<td>Womens</td>
<td>.65935</td>
</tr>
<tr>
<td><b>84</b></td>
<td>108</td>
<td>Dub City Derby Girls</td>
<td>Dub City</td>
<td>Womens</td>
<td>.65836</td>
</tr>
<tr>
<td><b>85</b></td>
<td>109</td>
<td>San Diego Roller Derby</td>
<td>San Diego Starlettes</td>
<td>Womens</td>
<td>.65733</td>
</tr>
<tr>
<td><b>86</b></td>
<td>110</td>
<td>Central City Roller Girls</td>
<td>Central City</td>
<td>Womens</td>
<td>.65727</td>
</tr>
<tr>
<td><b>87</b></td>
<td>111</td>
<td>Kansas City Roller Warriors</td>
<td>Kansas City</td>
<td>Womens</td>
<td>.65721</td>
</tr>
<tr>
<td><b>88</b></td>
<td>112</td>
<td>E-Ville Roller Derby</td>
<td>E-Ville</td>
<td>Womens</td>
<td>.65683</td>
</tr>
<tr>
<td><b>89</b></td>
<td>114</td>
<td>Western Australia Roller Derby</td>
<td>Western Australia</td>
<td>Womens</td>
<td>.65356</td>
</tr>
<tr>
<td><b>90</b></td>
<td>115</td>
<td>Bandoleras</td>
<td>Tucson</td>
<td>Womens</td>
<td>.65223</td>
</tr>
<tr>
<td><b>91</b></td>
<td>116</td>
<td>Dirty River Roller Grrrls</td>
<td>Dirty River</td>
<td>Womens</td>
<td>.65054</td>
</tr>
<tr>
<td><b>92</b></td>
<td>117</td>
<td>Oklahoma Victory Dolls</td>
<td>Okla. Victory</td>
<td>Womens</td>
<td>.64984</td>
</tr>
<tr>
<td><b>93</b></td>
<td>118</td>
<td>Rideau Valley Roller Girls</td>
<td>Rideau Valley</td>
<td>Womens</td>
<td>.64951</td>
</tr>
<tr>
<td><b>94</b></td>
<td>119</td>
<td>V Town Derby Dames</td>
<td>V Town</td>
<td>Womens</td>
<td>.64868</td>
</tr>
<tr>
<td><b>95</b></td>
<td>121</td>
<td>Sac City Rollers</td>
<td>Sac City</td>
<td>Womens</td>
<td>.64738</td>
</tr>
<tr>
<td><b>96</b></td>
<td>122</td>
<td>Copenhagen Roller Derby</td>
<td>Copenhagen</td>
<td>Womens</td>
<td>.64726</td>
</tr>
<tr>
<td><b>97</b></td>
<td>123</td>
<td>Nidaros Roller Derby</td>
<td>Nidaros</td>
<td>Womens</td>
<td>.64608</td>
</tr>
<tr>
<td><b>98</b></td>
<td>125</td>
<td>Rain of Terror</td>
<td>Rat City</td>
<td>Womens</td>
<td>.64488</td>
</tr>
<tr>
<td><b>99</b></td>
<td>126</td>
<td>Hot Wheel Roller Derby</td>
<td>Hot Wheel</td>
<td>Womens</td>
<td>.64428</td>
</tr>
<tr>
<td><b>100</b></td>
<td>128</td>
<td>Birmingham Blitz Dames</td>
<td>Blitz Dames</td>
<td>Womens</td>
<td>.64286</td>
</tr>
<tr>
<td><b>101</b></td>
<td>131</td>
<td>Treasure Valley Roller Derby Inc.</td>
<td>Treasure Valley</td>
<td>Womens</td>
<td>.64160</td>
</tr>
<tr>
<td><b>102</b></td>
<td>132</td>
<td>Les Sexpos</td>
<td>Montreal</td>
<td>Womens</td>
<td>.63986</td>
</tr>
<tr>
<td><b>103</b></td>
<td>134</td>
<td>One Love Roller Dolls</td>
<td>Antwerp</td>
<td>Womens</td>
<td>.63877</td>
</tr>
<tr>
<td><b>104</b></td>
<td>135</td>
<td>Leeds Roller Dolls</td>
<td>Leeds</td>
<td>Womens</td>
<td>.63770</td>
</tr>
<tr>
<td><b>105</b></td>
<td>136</td>
<td>Rumble Bs</td>
<td>Atlanta</td>
<td>Womens</td>
<td>.63769</td>
</tr>
<tr>
<td><b>106</b></td>
<td>139</td>
<td>Crime City B Team</td>
<td>Crime City</td>
<td>Womens</td>
<td>.63651</td>
</tr>
<tr>
<td><b>107</b></td>
<td>140</td>
<td>Motor City Disassembly Line</td>
<td>Detroit</td>
<td>Womens</td>
<td>.63598</td>
</tr>
<tr>
<td><b>108</b></td>
<td>141</td>
<td>Capital City Derby Dolls</td>
<td>Capital City</td>
<td>Womens</td>
<td>.63560</td>
</tr>
<tr>
<td><b>109</b></td>
<td>142</td>
<td>Helsinki Queen B’s</td>
<td>Helsinki</td>
<td>Womens</td>
<td>.63551</td>
</tr>
<tr>
<td><b>110</b></td>
<td>143</td>
<td>Granite City Roller Derby</td>
<td>Granite City</td>
<td>Womens</td>
<td>.63520</td>
</tr>
<tr>
<td><b>111</b></td>
<td>144</td>
<td>Cincinnati Rollergirls</td>
<td>Cincinnati</td>
<td>Womens</td>
<td>.63379</td>
</tr>
<tr>
<td><b>112</b></td>
<td>145</td>
<td>Brisbane City Rollers</td>
<td>Brisbane City</td>
<td>Womens</td>
<td>.63129</td>
</tr>
<tr>
<td><b>113</b></td>
<td>146</td>
<td>The Chicago Outfit Roller Derby</td>
<td>Chicago Outfit</td>
<td>Womens</td>
<td>.62964</td>
</tr>
<tr>
<td><b>114</b></td>
<td>147</td>
<td>Happy Valley Derby Darlins</td>
<td>Happy Valley</td>
<td>Womens</td>
<td>.62856</td>
</tr>
<tr>
<td><b>115</b></td>
<td>148</td>
<td>Omaha Rollergirls</td>
<td>Omaha</td>
<td>Womens</td>
<td>.62837</td>
</tr>
<tr>
<td><b>116</b></td>
<td>149</td>
<td>Undead Bettys Roller Derby</td>
<td>Undead Bettys</td>
<td>Womens</td>
<td>.62779</td>
</tr>
<tr>
<td><b>117</b></td>
<td>151</td>
<td>Gent Go Go Roller Girls</td>
<td>Gent Go Go</td>
<td>Womens</td>
<td>.62625</td>
</tr>
<tr>
<td><b>118</b></td>
<td>152</td>
<td>Winnipeg Roller Derby League</td>
<td>Winnipeg</td>
<td>Womens</td>
<td>.62547</td>
</tr>
<tr>
<td><b>119</b></td>
<td>153</td>
<td>Saint Lunachix</td>
<td>Arch Rival</td>
<td>Womens</td>
<td>.62251</td>
</tr>
<tr>
<td><b>120</b></td>
<td>154</td>
<td>Mother State Roller Derby</td>
<td>Mother State</td>
<td>Womens</td>
<td>.62225</td>
</tr>
<tr>
<td><b>121</b></td>
<td>155</td>
<td>North Star Roller Girls</td>
<td>North Star</td>
<td>Womens</td>
<td>.62097</td>
</tr>
<tr>
<td><b>122</b></td>
<td>157</td>
<td>Carolina Rollergirls</td>
<td>Carolina</td>
<td>Womens</td>
<td>.61999</td>
</tr>
<tr>
<td><b>123</b></td>
<td>158</td>
<td>Maine Roller Derby</td>
<td>Maine</td>
<td>Womens</td>
<td>.61940</td>
</tr>
<tr>
<td><b>124</b></td>
<td>159</td>
<td>Muddy River Rollers</td>
<td>Muddy River</td>
<td>Womens</td>
<td>.61877</td>
</tr>
<tr>
<td><b>125</b></td>
<td>160</td>
<td>Twin City Derby Girls</td>
<td>Twin City</td>
<td>Womens</td>
<td>.61664</td>
</tr>
<tr>
<td><b>126</b></td>
<td>162</td>
<td>The Rolling Candies</td>
<td>Rolling Candies</td>
<td>Womens</td>
<td>.61494</td>
</tr>
<tr>
<td><b>127</b></td>
<td>163</td>
<td>San Fernando Valley Roller Derby</td>
<td>San Fernando</td>
<td>Womens</td>
<td>.61428</td>
</tr>
<tr>
<td><b>128</b></td>
<td>164</td>
<td>Grand Raggidy Roller Derby</td>
<td>Grand Raggidy</td>
<td>Womens</td>
<td>.61410</td>
</tr>
<tr>
<td><b>129</b></td>
<td>165</td>
<td>Gothenburg Roller Derby</td>
<td>Gothenburg</td>
<td>Womens</td>
<td>.61230</td>
</tr>
<tr>
<td><b>130</b></td>
<td>166</td>
<td>Mainland Misfits</td>
<td>Mainland Misfits</td>
<td>Womens</td>
<td>.61105</td>
</tr>
<tr>
<td><b>131</b></td>
<td>167</td>
<td>Sonoma County Roller Derby</td>
<td>Sonoma</td>
<td>Womens</td>
<td>.61076</td>
</tr>
<tr>
<td><b>132</b></td>
<td>168</td>
<td>Roller Derby Quebec</td>
<td>Quebec</td>
<td>Womens</td>
<td>.60993</td>
</tr>
<tr>
<td><b>133</b></td>
<td>169</td>
<td>Notorious V.I.Cs</td>
<td>Victoria</td>
<td>Womens</td>
<td>.60826</td>
</tr>
<tr>
<td><b>134</b></td>
<td>170</td>
<td>Amsterdam Roller Derby</td>
<td>Amsterdam</td>
<td>Womens</td>
<td>.60735</td>
</tr>
<tr>
<td><b>135</b></td>
<td>171</td>
<td>Pikes Peak Derby Dames</td>
<td>Pikes Peak</td>
<td>Womens</td>
<td>.60667</td>
</tr>
<tr>
<td><b>136</b></td>
<td>172</td>
<td>Bristol Roller Derby (Women's)</td>
<td>Bristol A</td>
<td>Womens</td>
<td>.60536</td>
</tr>
<tr>
<td><b>137</b></td>
<td>173</td>
<td>DC Rollergirls</td>
<td>DC</td>
<td>Womens</td>
<td>.60497</td>
</tr>
<tr>
<td><b>138</b></td>
<td>175</td>
<td>Bogota Bonebreakers</td>
<td>Bogota Bonebreakers</td>
<td>Womens</td>
<td>.60037</td>
</tr>
<tr>
<td><b>139</b></td>
<td>176</td>
<td>Ithaca League of Women Rollers</td>
<td>Ithaca</td>
<td>Womens</td>
<td>.59927</td>
</tr>
<tr>
<td><b>140</b></td>
<td>178</td>
<td>Minnesota Nice</td>
<td>Minnesota</td>
<td>Womens</td>
<td>.59732</td>
</tr>
<tr>
<td><b>141</b></td>
<td>179</td>
<td>High Altitude Roller Derby</td>
<td>High Altitude</td>
<td>Womens</td>
<td>.59704</td>
</tr>
<tr>
<td><b>142</b></td>
<td>181</td>
<td>Battalion of Doom</td>
<td>Dallas</td>
<td>Womens</td>
<td>.59678</td>
</tr>
<tr>
<td><b>143</b></td>
<td>182</td>
<td>St. Pauli Roller Derby</td>
<td>St. Pauli</td>
<td>Womens</td>
<td>.59499</td>
</tr>
<tr>
<td><b>144</b></td>
<td>183</td>
<td>Tampere Roller Derby</td>
<td>Tampere</td>
<td>Womens</td>
<td>.59488</td>
</tr>
<tr>
<td><b>145</b></td>
<td>184</td>
<td>Berzerkers</td>
<td>Mass Maelstrom</td>
<td>Womens</td>
<td>.59463</td>
</tr>
<tr>
<td><b>146</b></td>
<td>185</td>
<td>Los Angeles Derby Dolls</td>
<td>LA Derby Dolls</td>
<td>Womens</td>
<td>.59252</td>
</tr>
<tr>
<td><b>147</b></td>
<td>186</td>
<td>Phoenix Rising</td>
<td>Arizona</td>
<td>Womens</td>
<td>.59155</td>
</tr>
<tr>
<td><b>148</b></td>
<td>187</td>
<td>Garden State Rollergirls</td>
<td>Garden State</td>
<td>Womens</td>
<td>.59148</td>
</tr>
<tr>
<td><b>149</b></td>
<td>188</td>
<td>Toronto Roller Derby</td>
<td>Toronto</td>
<td>Womens</td>
<td>.59139</td>
</tr>
<tr>
<td><b>150</b></td>
<td>189</td>
<td>Fort Myers Derby Girls</td>
<td>Ft. Myers</td>
<td>Womens</td>
<td>.59020</td>
</tr>
<tr>
<td><b>151</b></td>
<td>190</td>
<td>Emerald City Roller Derby</td>
<td>Emerald City</td>
<td>Womens</td>
<td>.58913</td>
</tr>
<tr>
<td><b>152</b></td>
<td>191</td>
<td>Monterey Bay Derby Dames</td>
<td>Monterey Bay</td>
<td>Womens</td>
<td>.58806</td>
</tr>
<tr>
<td><b>153</b></td>
<td>192</td>
<td>Gem City Rollergirls</td>
<td>Gem City</td>
<td>Womens</td>
<td>.58609</td>
</tr>
<tr>
<td><b>154</b></td>
<td>194</td>
<td>Dairyland Doll B-team</td>
<td>Madison</td>
<td>Womens</td>
<td>.58597</td>
</tr>
<tr>
<td><b>155</b></td>
<td>195</td>
<td>SoCal Derby</td>
<td>SoCal</td>
<td>Womens</td>
<td>.58584</td>
</tr>
<tr>
<td><b>156</b></td>
<td>196</td>
<td>Pirate City Rollers</td>
<td>Pirate City</td>
<td>Womens</td>
<td>.58450</td>
</tr>
<tr>
<td><b>157</b></td>
<td>197</td>
<td>Blue Ribbon Bullies</td>
<td>Team United</td>
<td>Womens</td>
<td>.58341</td>
</tr>
<tr>
<td><b>158</b></td>
<td>198</td>
<td>Boston B Party</td>
<td>Boston</td>
<td>Womens</td>
<td>.58310</td>
</tr>
<tr>
<td><b>159</b></td>
<td>199</td>
<td>Richter City Roller Derby</td>
<td>Richter City</td>
<td>Womens</td>
<td>.58283</td>
</tr>
<tr>
<td><b>160</b></td>
<td>200</td>
<td>Saint Chux Derby Chix</td>
<td>St. Chux</td>
<td>Womens</td>
<td>.58168</td>
</tr>
<tr>
<td><b>161</b></td>
<td>201</td>
<td>Royal City Roller Girls</td>
<td>Royal City</td>
<td>Womens</td>
<td>.58146</td>
</tr>
<tr>
<td><b>162</b></td>
<td>203</td>
<td>Oslo Roller Derby</td>
<td>Oslo</td>
<td>Womens</td>
<td>.58068</td>
</tr>
<tr>
<td><b>163</b></td>
<td>204</td>
<td>Dublin Roller Derby B</td>
<td>Dublin</td>
<td>Womens</td>
<td>.57961</td>
</tr>
<tr>
<td><b>164</b></td>
<td>205</td>
<td>The Contenders</td>
<td>Rocky Mtn.</td>
<td>Womens</td>
<td>.57836</td>
</tr>
<tr>
<td><b>165</b></td>
<td>206</td>
<td>Swansea City Roller Derby</td>
<td>Swansea</td>
<td>Womens</td>
<td>.57834</td>
</tr>
<tr>
<td><b>166</b></td>
<td>207</td>
<td>Molly Roger Rollergirls</td>
<td>Molly Roger</td>
<td>Womens</td>
<td>.57817</td>
</tr>
<tr>
<td><b>167</b></td>
<td>208</td>
<td>Brussels Derby Pixies</td>
<td>Brussels (Womens)</td>
<td>Womens</td>
<td>.57654</td>
</tr>
<tr>
<td><b>168</b></td>
<td>209</td>
<td>Melbourne Northside Rollers</td>
<td>Melbourne Northside</td>
<td>Womens</td>
<td>.57598</td>
</tr>
<tr>
<td><b>169</b></td>
<td>210</td>
<td>Glasgow Roller Derby</td>
<td>Glasgow</td>
<td>Womens</td>
<td>.57597</td>
</tr>
<tr>
<td><b>170</b></td>
<td>211</td>
<td>Roller Derby Madrid</td>
<td>Madrid</td>
<td>Womens</td>
<td>.57549</td>
</tr>
<tr>
<td><b>171</b></td>
<td>212</td>
<td>Independence Dolls</td>
<td>Philly</td>
<td>Womens</td>
<td>.57509</td>
</tr>
<tr>
<td><b>172</b></td>
<td>213</td>
<td>Roller Derby Caen</td>
<td>Caen</td>
<td>Womens</td>
<td>.57473</td>
</tr>
<tr>
<td><b>173</b></td>
<td>214</td>
<td>Les Quedalles</td>
<td>Paris</td>
<td>Womens</td>
<td>.57449</td>
</tr>
<tr>
<td><b>174</b></td>
<td>215</td>
<td>Cheyenne Roller Derby</td>
<td>Capidoll Stars</td>
<td>Womens</td>
<td>.57418</td>
</tr>
<tr>
<td><b>175</b></td>
<td>216</td>
<td>Crossroads City Derby Girls</td>
<td>Crossroads City</td>
<td>Womens</td>
<td>.57411</td>
</tr>
<tr>
<td><b>176</b></td>
<td>217</td>
<td>Halifax Bruising Banditas</td>
<td>Banditas</td>
<td>Womens</td>
<td>.57395</td>
</tr>
<tr>
<td><b>177</b></td>
<td>218</td>
<td>Killamazoo Derby Darlins</td>
<td>Killamazoo</td>
<td>Womens</td>
<td>.57261</td>
</tr>
<tr>
<td><b>178</b></td>
<td>219</td>
<td>Brewcity Bruisers</td>
<td>Brewcity</td>
<td>Womens</td>
<td>.57095</td>
</tr>
<tr>
<td><b>179</b></td>
<td>220</td>
<td>Geelong Roller Derby League</td>
<td>Geelong</td>
<td>Womens</td>
<td>.57024</td>
</tr>
<tr>
<td><b>180</b></td>
<td>223</td>
<td>Stuttgart Valley Rollergirls</td>
<td>Stuttgart Valley</td>
<td>Womens</td>
<td>.56941</td>
</tr>
<tr>
<td><b>181</b></td>
<td>224</td>
<td>Providence Roller Derby</td>
<td>Providence</td>
<td>Womens</td>
<td>.56927</td>
</tr>
<tr>
<td><b>182</b></td>
<td>225</td>
<td>Monterey Bay Derby Dames</td>
<td>Monterey Bay</td>
<td>Womens</td>
<td>.56905</td>
</tr>
<tr>
<td><b>183</b></td>
<td>226</td>
<td>Northwest Arkansas Roller Derby</td>
<td>NW Arkansas</td>
<td>Womens</td>
<td>.56870</td>
</tr>
<tr>
<td><b>184</b></td>
<td>227</td>
<td>Spa Town Roller Girls</td>
<td>Spa Town</td>
<td>Womens</td>
<td>.56802</td>
</tr>
<tr>
<td><b>185</b></td>
<td>228</td>
<td>Roc City Roller Derby</td>
<td>Roc City</td>
<td>Womens</td>
<td>.56757</td>
</tr>
<tr>
<td><b>186</b></td>
<td>229</td>
<td>Cape Fear Roller Girls</td>
<td>Cape Fear</td>
<td>Womens</td>
<td>.56577</td>
</tr>
<tr>
<td><b>187</b></td>
<td>230</td>
<td>Palouse River Rollers</td>
<td>Palouse</td>
<td>Womens</td>
<td>.56514</td>
</tr>
<tr>
<td><b>188</b></td>
<td>231</td>
<td>Beckley Area Derby Dames</td>
<td>Beckley</td>
<td>Womens</td>
<td>.56441</td>
</tr>
<tr>
<td><b>189</b></td>
<td>233</td>
<td>SAM Roller Derby (Women's)</td>
<td>All Blocks</td>
<td>Womens</td>
<td>.56382</td>
</tr>
<tr>
<td><b>190</b></td>
<td>234</td>
<td>Namur Roller Girls</td>
<td>Namur</td>
<td>Womens</td>
<td>.56296</td>
</tr>
<tr>
<td><b>191</b></td>
<td>235</td>
<td>Tender Hooligans</td>
<td>Rainy City (UK)</td>
<td>Womens</td>
<td>.56291</td>
</tr>
<tr>
<td><b>192</b></td>
<td>236</td>
<td>Fabulous Sin City Rollergirls</td>
<td>Sin City</td>
<td>Womens</td>
<td>.56256</td>
</tr>
<tr>
<td><b>193</b></td>
<td>237</td>
<td>Cambridge Rollerbillies</td>
<td>Cambridge</td>
<td>Womens</td>
<td>.56250</td>
</tr>
<tr>
<td><b>194</b></td>
<td>238</td>
<td>Rated PG Rollergirls</td>
<td>Northstar</td>
<td>Womens</td>
<td>.56195</td>
</tr>
<tr>
<td><b>195</b></td>
<td>239</td>
<td>Oulu Roller Derby</td>
<td>Oulu</td>
<td>Womens</td>
<td>.56132</td>
</tr>
<tr>
<td><b>196</b></td>
<td>240</td>
<td>London Rockin' Rollers</td>
<td>Rockin' Rollers</td>
<td>Womens</td>
<td>.56130</td>
</tr>
<tr>
<td><b>197</b></td>
<td>241</td>
<td>Long Island Roller Rebels</td>
<td>Long Island</td>
<td>Womens</td>
<td>.56109</td>
</tr>
<tr>
<td><b>198</b></td>
<td>242</td>
<td>Dead End Derby</td>
<td>Dead End</td>
<td>Womens</td>
<td>.56068</td>
</tr>
<tr>
<td><b>199</b></td>
<td>243</td>
<td>Nottingham Hellfire Harlots</td>
<td>Nottingham Hellfire Harlots</td>
<td>Womens</td>
<td>.55939</td>
</tr>
<tr>
<td><b>200</b></td>
<td>244</td>
<td>Lehigh Valley Rollergirls</td>
<td>Lehigh Valley</td>
<td>Womens</td>
<td>.55796</td>
</tr>
<tr>
<td><b>201</b></td>
<td>245</td>
<td>Royal Windsor Roller Girls</td>
<td>Royal Windsor</td>
<td>Womens</td>
<td>.55783</td>
</tr>
<tr>
<td><b>202</b></td>
<td>246</td>
<td>Silicon Valley Rollergirls</td>
<td>Silicon Valley</td>
<td>Womens</td>
<td>.55725</td>
</tr>
<tr>
<td><b>203</b></td>
<td>247</td>
<td>South Coast Roller Derby</td>
<td>South Coast</td>
<td>Womens</td>
<td>.55662</td>
</tr>
<tr>
<td><b>204</b></td>
<td>248</td>
<td>Granite State Roller Derby</td>
<td>Granite State</td>
<td>Womens</td>
<td>.55653</td>
</tr>
<tr>
<td><b>205</b></td>
<td>249</td>
<td>Norrköping Roller Derby</td>
<td>Norrköping</td>
<td>Womens</td>
<td>.55645</td>
</tr>
<tr>
<td><b>206</b></td>
<td>250</td>
<td>Fort Wayne Derby Girls</td>
<td>Ft. Wayne</td>
<td>Womens</td>
<td>.55552</td>
</tr>
<tr>
<td><b>207</b></td>
<td>251</td>
<td>Liverpool Roller Birds</td>
<td>Liverpool</td>
<td>Womens</td>
<td>.55478</td>
</tr>
<tr>
<td><b>208</b></td>
<td>252</td>
<td>Bakersfield Diamond Divas</td>
<td>Diamond Divas</td>
<td>Womens</td>
<td>.55379</td>
</tr>
<tr>
<td><b>209</b></td>
<td>253</td>
<td>Auckland Roller Derby League</td>
<td>Auckland</td>
<td>Womens</td>
<td>.55330</td>
</tr>
<tr>
<td><b>210</b></td>
<td>254</td>
<td>Sierra Regional Roller Derby</td>
<td>Sierra</td>
<td>Womens</td>
<td>.55253</td>
</tr>
<tr>
<td><b>211</b></td>
<td>255</td>
<td>Tenerife Roller Derby</td>
<td>Tenerife</td>
<td>Womens</td>
<td>.55251</td>
</tr>
<tr>
<td><b>212</b></td>
<td>256</td>
<td>Manchester Roller Derby (Women's)</td>
<td>Manchester</td>
<td>Womens</td>
<td>.55017</td>
</tr>
<tr>
<td><b>213</b></td>
<td>257</td>
<td>Eves of Destruction</td>
<td>Eves of Destruction</td>
<td>Womens</td>
<td>.54950</td>
</tr>
<tr>
<td><b>214</b></td>
<td>258</td>
<td>Junction City Roller Dolls</td>
<td>Junction City</td>
<td>Womens</td>
<td>.54918</td>
</tr>
<tr>
<td><b>215</b></td>
<td>259</td>
<td>Green Mountain Roller Derby</td>
<td>Green Mt.</td>
<td>Womens</td>
<td>.54810</td>
</tr>
<tr>
<td><b>216</b></td>
<td>260</td>
<td>Second Wind</td>
<td>Windy City</td>
<td>Womens</td>
<td>.54796</td>
</tr>
<tr>
<td><b>217</b></td>
<td>261</td>
<td>Les Quads de Paris Roller Derby</td>
<td>Quads de Paris</td>
<td>Womens</td>
<td>.54756</td>
</tr>
<tr>
<td><b>218</b></td>
<td>263</td>
<td>Bairn City Rollers (Women's)</td>
<td>Central Belters</td>
<td>Womens</td>
<td>.54635</td>
</tr>
<tr>
<td><b>219</b></td>
<td>264</td>
<td>Lansing Derby Vixens</td>
<td>Lansing Vixens</td>
<td>Womens</td>
<td>.54573</td>
</tr>
<tr>
<td><b>220</b></td>
<td>265</td>
<td>DuPage Derby Dames</td>
<td>DuPage Derby</td>
<td>Womens</td>
<td>.54553</td>
</tr>
<tr>
<td><b>221</b></td>
<td>266</td>
<td>London Batter C Power</td>
<td>London</td>
<td>Womens</td>
<td>.54491</td>
</tr>
<tr>
<td><b>222</b></td>
<td>267</td>
<td>South Sea Roller Derby</td>
<td>South Sea</td>
<td>Womens</td>
<td>.54470</td>
</tr>
<tr>
<td><b>223</b></td>
<td>268</td>
<td>Roller Derby Porto</td>
<td>Porto</td>
<td>Womens</td>
<td>.54403</td>
</tr>
<tr>
<td><b>224</b></td>
<td>269</td>
<td>Powder River Rousta Bout It Betties</td>
<td>Powder River</td>
<td>Womens</td>
<td>.54391</td>
</tr>
<tr>
<td><b>225</b></td>
<td>270</td>
<td>Roller Derby Dresden</td>
<td>Dresden</td>
<td>Womens</td>
<td>.54223</td>
</tr>
<tr>
<td><b>226</b></td>
<td>271</td>
<td>Warning Belles</td>
<td>Naptown</td>
<td>Womens</td>
<td>.53966</td>
</tr>
<tr>
<td><b>227</b></td>
<td>272</td>
<td>Hellgate Roller Derby</td>
<td>Hellgate</td>
<td>Womens</td>
<td>.53857</td>
</tr>
<tr>
<td><b>228</b></td>
<td>273</td>
<td>Pit Crew</td>
<td>Cherry City</td>
<td>Womens</td>
<td>.53853</td>
</tr>
<tr>
<td><b>229</b></td>
<td>276</td>
<td>Tiger Bay B-Bombs</td>
<td>Tiger Bay</td>
<td>Womens</td>
<td>.53746</td>
</tr>
<tr>
<td><b>230</b></td>
<td>277</td>
<td>Dominion Derby Girls</td>
<td>Dominion</td>
<td>Womens</td>
<td>.53739</td>
</tr>
<tr>
<td><b>231</b></td>
<td>278</td>
<td>Furness Firecrackers (Women's)</td>
<td>Furness Women's</td>
<td>Womens</td>
<td>.53705</td>
</tr>
<tr>
<td><b>232</b></td>
<td>279</td>
<td>Bay State Brawlers</td>
<td>Bay State Brawlers</td>
<td>Womens</td>
<td>.53702</td>
</tr>
<tr>
<td><b>233</b></td>
<td>280</td>
<td>South West Angels of Terror</td>
<td>Angels of Terror</td>
<td>Womens</td>
<td>.53682</td>
</tr>
<tr>
<td><b>234</b></td>
<td>281</td>
<td>Burning River Roller Derby</td>
<td>Burning River</td>
<td>Womens</td>
<td>.53629</td>
</tr>
<tr>
<td><b>235</b></td>
<td>282</td>
<td>ICT Roller Girls</td>
<td>ICT</td>
<td>Womens</td>
<td>.53600</td>
</tr>
<tr>
<td><b>236</b></td>
<td>283</td>
<td>Northern Brisbane Rollers</td>
<td>Northern Brisbane</td>
<td>Womens</td>
<td>.53568</td>
</tr>
<tr>
<td><b>237</b></td>
<td>284</td>
<td>Oklahoma City Roller Derby</td>
<td>Oklahoma City</td>
<td>Womens</td>
<td>.53490</td>
</tr>
<tr>
<td><b>238</b></td>
<td>285</td>
<td>Cornfed Derby Dames</td>
<td>Cornfed</td>
<td>Womens</td>
<td>.53347</td>
</tr>
<tr>
<td><b>239</b></td>
<td>286</td>
<td>Portsmouth Roller Wenches</td>
<td>Portsmouth</td>
<td>Womens</td>
<td>.53345</td>
</tr>
<tr>
<td><b>240</b></td>
<td>287</td>
<td>Central NY Roller Derby</td>
<td>Central NY</td>
<td>Womens</td>
<td>.53282</td>
</tr>
<tr>
<td><b>241</b></td>
<td>288</td>
<td>Limerick Roller Derby</td>
<td>Limerick</td>
<td>Womens</td>
<td>.53231</td>
</tr>
<tr>
<td><b>242</b></td>
<td>289</td>
<td>Rockcity Rollers</td>
<td>Rockcity</td>
<td>Womens</td>
<td>.53133</td>
</tr>
<tr>
<td><b>243</b></td>
<td>290</td>
<td>Bangor Roller Derby</td>
<td>Bangor</td>
<td>Womens</td>
<td>.53112</td>
</tr>
<tr>
<td><b>244</b></td>
<td>291</td>
<td>The Royal Swedish Roller Derby</td>
<td>The Royal Army</td>
<td>Womens</td>
<td>.53092</td>
</tr>
<tr>
<td><b>245</b></td>
<td>292</td>
<td>Gorge Roller Girls</td>
<td>Gorge Roller Girls</td>
<td>Womens</td>
<td>.53084</td>
</tr>
<tr>
<td><b>246</b></td>
<td>293</td>
<td>Salisbury Roller Girls</td>
<td>Salisbury</td>
<td>Womens</td>
<td>.53070</td>
</tr>
<tr>
<td><b>247</b></td>
<td>294</td>
<td>Darlings</td>
<td>V Town</td>
<td>Womens</td>
<td>.53065</td>
</tr>
<tr>
<td><b>248</b></td>
<td>295</td>
<td>Luleå Roller Derby</td>
<td>Luleå</td>
<td>Womens</td>
<td>.52965</td>
</tr>
<tr>
<td><b>249</b></td>
<td>296</td>
<td>Arbor Bruising Co.</td>
<td>Ann Arbor</td>
<td>Womens</td>
<td>.52953</td>
</tr>
<tr>
<td><b>250</b></td>
<td>297</td>
<td>Ventura County Derby Darlins</td>
<td>Ventura</td>
<td>Womens</td>
<td>.52942</td>
</tr>
<tr>
<td><b>251</b></td>
<td>298</td>
<td>SINtral Valley Derby Girls</td>
<td>SINtral Valley</td>
<td>Womens</td>
<td>.52805</td>
</tr>
<tr>
<td><b>252</b></td>
<td>299</td>
<td>Tallahassee Rollergirls</td>
<td>Tallahassee</td>
<td>Womens</td>
<td>.52584</td>
</tr>
<tr>
<td><b>253</b></td>
<td>300</td>
<td>Bleeding Heartland Roller Derby</td>
<td>Bleeding Heartland</td>
<td>Womens</td>
<td>.52579</td>
</tr>
<tr>
<td><b>254</b></td>
<td>301</td>
<td>Blocka Nostra</td>
<td>Toulouse</td>
<td>Womens</td>
<td>.52460</td>
</tr>
<tr>
<td><b>255</b></td>
<td>302</td>
<td>Downriver Roller Dolls</td>
<td>Downriver</td>
<td>Womens</td>
<td>.52448</td>
</tr>
<tr>
<td><b>256</b></td>
<td>303</td>
<td>10th Mountain Roller Dolls</td>
<td>10th Mtn.</td>
<td>Womens</td>
<td>.52387</td>
</tr>
<tr>
<td><b>257</b></td>
<td>304</td>
<td>Croydon Roller Derby</td>
<td>Croydon</td>
<td>Womens</td>
<td>.52364</td>
</tr>
<tr>
<td><b>258</b></td>
<td>305</td>
<td>Cherry City Derby Girls</td>
<td>Cherry City</td>
<td>Womens</td>
<td>.52300</td>
</tr>
<tr>
<td><b>259</b></td>
<td>306</td>
<td>Killer Bees</td>
<td>Sun State</td>
<td>Womens</td>
<td>.52292</td>
</tr>
<tr>
<td><b>260</b></td>
<td>307</td>
<td>Varsity Derby League</td>
<td>Varsity</td>
<td>Womens</td>
<td>.52260</td>
</tr>
<tr>
<td><b>261</b></td>
<td>308</td>
<td>Connecticut RollerGirls</td>
<td>Connecticut</td>
<td>Womens</td>
<td>.52259</td>
</tr>
<tr>
<td><b>262</b></td>
<td>309</td>
<td>Vienna Roller Derby</td>
<td>Vienna</td>
<td>Womens</td>
<td>.52250</td>
</tr>
<tr>
<td><b>263</b></td>
<td>310</td>
<td>Lava City Roller Dolls</td>
<td>Lava City</td>
<td>Womens</td>
<td>.52246</td>
</tr>
<tr>
<td><b>264</b></td>
<td>311</td>
<td>Folsom Prison Bruisers</td>
<td>Sac City</td>
<td>Womens</td>
<td>.52236</td>
</tr>
<tr>
<td><b>265</b></td>
<td>313</td>
<td>Wheat City Roller Derby</td>
<td>Wheat City</td>
<td>Womens</td>
<td>.52182</td>
</tr>
<tr>
<td><b>266</b></td>
<td>314</td>
<td>Dundee Roller Girls</td>
<td>Dundee</td>
<td>Womens</td>
<td>.52101</td>
</tr>
<tr>
<td><b>267</b></td>
<td>315</td>
<td>Little City Rollergirls</td>
<td>Little City</td>
<td>Womens</td>
<td>.52099</td>
</tr>
<tr>
<td><b>268</b></td>
<td>317</td>
<td>A-Stars B Team</td>
<td>Toronto</td>
<td>Womens</td>
<td>.52056</td>
</tr>
<tr>
<td><b>269</b></td>
<td>318</td>
<td>Newcastle Roller Derby League</td>
<td>Newcastle</td>
<td>Womens</td>
<td>.52011</td>
</tr>
<tr>
<td><b>270</b></td>
<td>319</td>
<td>Duke City Roller Derby</td>
<td>Duke</td>
<td>Womens</td>
<td>.51986</td>
</tr>
<tr>
<td><b>271</b></td>
<td>320</td>
<td>Inglorious Bombshells</td>
<td>Bear City</td>
<td>Womens</td>
<td>.51980</td>
</tr>
<tr>
<td><b>272</b></td>
<td>321</td>
<td>Snipers</td>
<td>Sydney Assassins</td>
<td>Womens</td>
<td>.51976</td>
</tr>
<tr>
<td><b>273</b></td>
<td>322</td>
<td>Gold Coast Derby Grrls</td>
<td>Gold Coast (FL)</td>
<td>Womens</td>
<td>.51927</td>
</tr>
<tr>
<td><b>274</b></td>
<td>323</td>
<td>Squamish Women's Roller Derby</td>
<td>Squamish</td>
<td>Womens</td>
<td>.51820</td>
</tr>
<tr>
<td><b>275</b></td>
<td>324</td>
<td>Red Stick Roller Derby</td>
<td>Red Stick</td>
<td>Womens</td>
<td>.51784</td>
</tr>
<tr>
<td><b>276</b></td>
<td>325</td>
<td>Shasta Roller Derby</td>
<td>Shasta</td>
<td>Womens</td>
<td>.51779</td>
</tr>
<tr>
<td><b>277</b></td>
<td>326</td>
<td>Lutece Destroyeuses Roller Derby Paris</td>
<td>Lutece</td>
<td>Womens</td>
<td>.51762</td>
</tr>
<tr>
<td><b>278</b></td>
<td>327</td>
<td>River City Rat Pack</td>
<td>Jacksonville</td>
<td>Womens</td>
<td>.51761</td>
</tr>
<tr>
<td><b>279</b></td>
<td>328</td>
<td>Rock Coast Rollers</td>
<td>Rock Coast</td>
<td>Womens</td>
<td>.51752</td>
</tr>
<tr>
<td><b>280</b></td>
<td>329</td>
<td>Dunedin Derby</td>
<td>Dunedin</td>
<td>Womens</td>
<td>.51696</td>
</tr>
<tr>
<td><b>281</b></td>
<td>330</td>
<td>Ark Valley High Rollers</td>
<td>Ark Valley</td>
<td>Womens</td>
<td>.51657</td>
</tr>
<tr>
<td><b>282</b></td>
<td>331</td>
<td>Big Easy Rollergirls</td>
<td>Big Easy</td>
<td>Womens</td>
<td>.51593</td>
</tr>
<tr>
<td><b>283</b></td>
<td>332</td>
<td>Coastal Assassins Roller Derby</td>
<td>Coastal Assassins</td>
<td>Womens</td>
<td>.51580</td>
</tr>
<tr>
<td><b>284</b></td>
<td>333</td>
<td>Naughty Pines Derby Dames</td>
<td>Naughty Pines</td>
<td>Womens</td>
<td>.51548</td>
</tr>
<tr>
<td><b>285</b></td>
<td>334</td>
<td>Rockin' City Rollergirls</td>
<td>Rockin' City</td>
<td>Womens</td>
<td>.51518</td>
</tr>
<tr>
<td><b>286</b></td>
<td>335</td>
<td>Terminal City B-Side</td>
<td>Terminal City</td>
<td>Womens</td>
<td>.51515</td>
</tr>
<tr>
<td><b>287</b></td>
<td>336</td>
<td>Bonneville Bone Crushers</td>
<td>Wasatch</td>
<td>Womens</td>
<td>.51505</td>
</tr>
<tr>
<td><b>288</b></td>
<td>337</td>
<td>Memphis Roller Derby</td>
<td>Memphis</td>
<td>Womens</td>
<td>.51503</td>
</tr>
<tr>
<td><b>289</b></td>
<td>338</td>
<td>Black Rose Rollers</td>
<td>Black Rose Rollers</td>
<td>Womens</td>
<td>.51418</td>
</tr>
<tr>
<td><b>290</b></td>
<td>339</td>
<td>Sitka Sound Slayers</td>
<td>Sitka</td>
<td>Womens</td>
<td>.51413</td>
</tr>
<tr>
<td><b>291</b></td>
<td>340</td>
<td>Brighton Rockers Roller Derby</td>
<td>Brighton (UK)</td>
<td>Womens</td>
<td>.51382</td>
</tr>
<tr>
<td><b>292</b></td>
<td>341</td>
<td>North Texas Roller Derby</td>
<td>North Texas</td>
<td>Womens</td>
<td>.51338</td>
</tr>
<tr>
<td><b>293</b></td>
<td>342</td>
<td>Roller Derby Rennes</td>
<td>Rennes</td>
<td>Womens</td>
<td>.51330</td>
</tr>
<tr>
<td><b>294</b></td>
<td>343</td>
<td>Standbys</td>
<td>Denver</td>
<td>Womens</td>
<td>.51300</td>
</tr>
<tr>
<td><b>295</b></td>
<td>344</td>
<td>Rock N Roller Queens</td>
<td>Rock N Roller Queens</td>
<td>Womens</td>
<td>.51283</td>
</tr>
<tr>
<td><b>296</b></td>
<td>345</td>
<td>Gallatin Roller Girlz</td>
<td>Gallatin Mayhem</td>
<td>Womens</td>
<td>.51269</td>
</tr>
<tr>
<td><b>297</b></td>
<td>346</td>
<td>KCRW Plan-B</td>
<td>Kansas City</td>
<td>Womens</td>
<td>.51247</td>
</tr>
<tr>
<td><b>298</b></td>
<td>347</td>
<td>Rainier Roller Girls</td>
<td>Rainier</td>
<td>Womens</td>
<td>.51240</td>
</tr>
<tr>
<td><b>299</b></td>
<td>348</td>
<td>Old Capitol City Roller Derby</td>
<td>Old Capitol City</td>
<td>Womens</td>
<td>.51186</td>
</tr>
<tr>
<td><b>300</b></td>
<td>349</td>
<td>Disciples</td>
<td>Sacred</td>
<td>Womens</td>
<td>.51185</td>
</tr>
<tr>
<td><b>301</b></td>
<td>350</td>
<td>Western MA Roller Derby</td>
<td>Western MA</td>
<td>Womens</td>
<td>.51143</td>
</tr>
<tr>
<td><b>302</b></td>
<td>351</td>
<td>Greenville Derby Dames</td>
<td>Greenville Derby Dames</td>
<td>Womens</td>
<td>.51097</td>
</tr>
<tr>
<td><b>303</b></td>
<td>352</td>
<td>Assassination City Roller Derby</td>
<td>Assassination</td>
<td>Womens</td>
<td>.51063</td>
</tr>
<tr>
<td><b>304</b></td>
<td>353</td>
<td>Unforgiven Roller Girls</td>
<td>Unforgiven</td>
<td>Womens</td>
<td>.51042</td>
</tr>
<tr>
<td><b>305</b></td>
<td>354</td>
<td>Northern Lights</td>
<td>North Star</td>
<td>Womens</td>
<td>.50997</td>
</tr>
<tr>
<td><b>306</b></td>
<td>355</td>
<td>Zurich City Rollergirlz</td>
<td>Zurich</td>
<td>Womens</td>
<td>.50977</td>
</tr>
<tr>
<td><b>307</b></td>
<td>356</td>
<td>Whakatane Roller Derby League</td>
<td>Whakatane</td>
<td>Womens</td>
<td>.50928</td>
</tr>
<tr>
<td><b>308</b></td>
<td>357</td>
<td>Jackson Hole Juggernauts</td>
<td>Juggernauts</td>
<td>Womens</td>
<td>.50921</td>
</tr>
<tr>
<td><b>309</b></td>
<td>358</td>
<td>Tri-City Plan B</td>
<td>Tri-City</td>
<td>Womens</td>
<td>.50885</td>
</tr>
<tr>
<td><b>310</b></td>
<td>359</td>
<td>Big Bucks High Rollers</td>
<td>High Rollers</td>
<td>Womens</td>
<td>.50870</td>
</tr>
<tr>
<td><b>311</b></td>
<td>360</td>
<td>Rising Rollers</td>
<td>Middlesbrough</td>
<td>Womens</td>
<td>.50857</td>
</tr>
<tr>
<td><b>312</b></td>
<td>361</td>
<td>Energetic City Roller Derby Association</td>
<td>Energetic City</td>
<td>Womens</td>
<td>.50827</td>
</tr>
<tr>
<td><b>313</b></td>
<td>362</td>
<td>Whippin' Hinnies</td>
<td>Newcastle</td>
<td>Womens</td>
<td>.50790</td>
</tr>
<tr>
<td><b>314</b></td>
<td>363</td>
<td>Bonnie Colliders</td>
<td>Dundee</td>
<td>Womens</td>
<td>.50780</td>
</tr>
<tr>
<td><b>315</b></td>
<td>364</td>
<td>Wirral Roller Derby</td>
<td>Wirral (Women's)</td>
<td>Womens</td>
<td>.50694</td>
</tr>
<tr>
<td><b>316</b></td>
<td>365</td>
<td>Sweetwater County Roller Derby</td>
<td>Bitter Sweet</td>
<td>Womens</td>
<td>.50641</td>
</tr>
<tr>
<td><b>317</b></td>
<td>367</td>
<td>Lowcountry Highrollers</td>
<td>Lowcountry</td>
<td>Womens</td>
<td>.50556</td>
</tr>
<tr>
<td><b>318</b></td>
<td>368</td>
<td>Faultline Derby Devilz</td>
<td>Faultline</td>
<td>Womens</td>
<td>.50459</td>
</tr>
<tr>
<td><b>319</b></td>
<td>369</td>
<td>Orcet Roller Derby</td>
<td>Orcet (Womens)</td>
<td>Womens</td>
<td>.50437</td>
</tr>
<tr>
<td><b>320</b></td>
<td>370</td>
<td>Derby Revolution of Bakersfield</td>
<td>Bakersfield</td>
<td>Womens</td>
<td>.50294</td>
</tr>
<tr>
<td><b>321</b></td>
<td>371</td>
<td>Billings Roller Derby Dames</td>
<td>Billings</td>
<td>Womens</td>
<td>.50202</td>
</tr>
<tr>
<td><b>322</b></td>
<td>372</td>
<td>Derby City Roller Girls</td>
<td>Derby City</td>
<td>Womens</td>
<td>.50198</td>
</tr>
<tr>
<td><b>323</b></td>
<td>373</td>
<td>Appalachian Rollergirls</td>
<td>Appalachian Rollergirls</td>
<td>Womens</td>
<td>.50102</td>
</tr>
<tr>
<td><b>324</b></td>
<td>374</td>
<td>Humboldt Roller Derby</td>
<td>Humboldt</td>
<td>Womens</td>
<td>.50066</td>
</tr>
<tr>
<td><b>325</b></td>
<td>375</td>
<td>The Switchblade RollerGrrrls</td>
<td>Switchblade</td>
<td>Womens</td>
<td>.50056</td>
</tr>
<tr>
<td><b>326</b></td>
<td>376</td>
<td>Rogue Rollergirls</td>
<td>Rogue Rollergirls</td>
<td>Womens</td>
<td>.50032</td>
</tr>
<tr>
<td><b>327</b></td>
<td>377</td>
<td>Hammer City Roller Girls</td>
<td>Hammer City</td>
<td>Womens</td>
<td>.49998</td>
</tr>
<tr>
<td><b>328</b></td>
<td>378</td>
<td>Fernie Roller Derby League</td>
<td>Avalanche City</td>
<td>Womens</td>
<td>.49971</td>
</tr>
<tr>
<td><b>329</b></td>
<td>379</td>
<td>Capidolls</td>
<td>Capidoll Stars</td>
<td>Womens</td>
<td>.49861</td>
</tr>
<tr>
<td><b>330</b></td>
<td>380</td>
<td>Charlotte Roller Girls</td>
<td>Charlotte</td>
<td>Womens</td>
<td>.49783</td>
</tr>
<tr>
<td><b>331</b></td>
<td>381</td>
<td>Chinook City Roller Derby (Women's)</td>
<td>Chinook City</td>
<td>Womens</td>
<td>.49774</td>
</tr>
<tr>
<td><b>332</b></td>
<td>383</td>
<td>Chattanooga Roller Girls</td>
<td>Chattanooga</td>
<td>Womens</td>
<td>.49710</td>
</tr>
<tr>
<td><b>333</b></td>
<td>384</td>
<td>Road Warriors</td>
<td>No Coast</td>
<td>Womens</td>
<td>.49672</td>
</tr>
<tr>
<td><b>334</b></td>
<td>386</td>
<td>Spit Fires</td>
<td>Lava City</td>
<td>Womens</td>
<td>.49523</td>
</tr>
<tr>
<td><b>335</b></td>
<td>387</td>
<td>FoCo Roller Derby</td>
<td>FoCo</td>
<td>Womens</td>
<td>.49522</td>
</tr>
<tr>
<td><b>336</b></td>
<td>388</td>
<td>Dom City Dolls</td>
<td>Dom City</td>
<td>Womens</td>
<td>.49522</td>
</tr>
<tr>
<td><b>337</b></td>
<td>389</td>
<td>Wine Country Crushers</td>
<td>Wine Country</td>
<td>Womens</td>
<td>.49489</td>
</tr>
<tr>
<td><b>338</b></td>
<td>391</td>
<td>Old Port Brigade</td>
<td>Maine</td>
<td>Womens</td>
<td>.49405</td>
</tr>
<tr>
<td><b>339</b></td>
<td>393</td>
<td>Barcelona Roller Derby</td>
<td>Barcelona</td>
<td>Womens</td>
<td>.49383</td>
</tr>
<tr>
<td><b>340</b></td>
<td>394</td>
<td>Classic City Rollergirls</td>
<td>Classic City</td>
<td>Womens</td>
<td>.49378</td>
</tr>
<tr>
<td><b>341</b></td>
<td>395</td>
<td>Fog City Rollers</td>
<td>Fog City</td>
<td>Womens</td>
<td>.49377</td>
</tr>
<tr>
<td><b>342</b></td>
<td>396</td>
<td>Blackpool Roller-Coasters</td>
<td>Blackpool</td>
<td>Womens</td>
<td>.49357</td>
</tr>
<tr>
<td><b>343</b></td>
<td>397</td>
<td>The Uppercuts</td>
<td>West Coast Knockouts</td>
<td>Womens</td>
<td>.49300</td>
</tr>
<tr>
<td><b>344</b></td>
<td>398</td>
<td>Heart Mountain Wreck on Wheels</td>
<td>Heart Mountain</td>
<td>Womens</td>
<td>.49291</td>
</tr>
<tr>
<td><b>345</b></td>
<td>399</td>
<td>Demolition City Roller Derby</td>
<td>Demolition</td>
<td>Womens</td>
<td>.49278</td>
</tr>
<tr>
<td><b>346</b></td>
<td>400</td>
<td>North Coast Nightmares</td>
<td>North Coast (BC)</td>
<td>Womens</td>
<td>.49223</td>
</tr>
<tr>
<td><b>347</b></td>
<td>401</td>
<td>All Star Reserves</td>
<td>Auld Reekie</td>
<td>Womens</td>
<td>.49204</td>
</tr>
<tr>
<td><b>348</b></td>
<td>402</td>
<td>Ruhrpott Roller Girls</td>
<td>Ruhrpott</td>
<td>Womens</td>
<td>.49105</td>
</tr>
<tr>
<td><b>349</b></td>
<td>403</td>
<td>Quad City Rollers</td>
<td>Quad City Rollers</td>
<td>Womens</td>
<td>.49078</td>
</tr>
<tr>
<td><b>350</b></td>
<td>405</td>
<td>Rotterdam Roller Derby</td>
<td>Rotterdam</td>
<td>Womens</td>
<td>.49019</td>
</tr>
<tr>
<td><b>351</b></td>
<td>406</td>
<td>North County Derby Alliance</td>
<td>North County</td>
<td>Womens</td>
<td>.48963</td>
</tr>
<tr>
<td><b>352</b></td>
<td>408</td>
<td>Tournament City Derby Dolls</td>
<td>Tournament City</td>
<td>Womens</td>
<td>.48888</td>
</tr>
<tr>
<td><b>353</b></td>
<td>409</td>
<td>The Cuttlefish</td>
<td>SoCal</td>
<td>Womens</td>
<td>.48879</td>
</tr>
<tr>
<td><b>354</b></td>
<td>410</td>
<td>Bullies</td>
<td>Hidden City</td>
<td>Womens</td>
<td>.48782</td>
</tr>
<tr>
<td><b>355</b></td>
<td>411</td>
<td>Magic City Rollers</td>
<td>Magic City Rollers</td>
<td>Womens</td>
<td>.48732</td>
</tr>
<tr>
<td><b>356</b></td>
<td>412</td>
<td>Derby Club le Cres Lattes Montpellier</td>
<td>Derby Club le Cres Lattes</td>
<td>Womens</td>
<td>.48706</td>
</tr>
<tr>
<td><b>357</b></td>
<td>413</td>
<td>Foothill Foxy Flyers</td>
<td>Foothill</td>
<td>Womens</td>
<td>.48672</td>
</tr>
<tr>
<td><b>358</b></td>
<td>414</td>
<td>All Star Rookies</td>
<td>Auld Reekie</td>
<td>Womens</td>
<td>.48609</td>
</tr>
<tr>
<td><b>359</b></td>
<td>415</td>
<td>Roller Derby Cáceres</td>
<td>Cáceres</td>
<td>Womens</td>
<td>.48596</td>
</tr>
<tr>
<td><b>360</b></td>
<td>416</td>
<td>Central Coast Roller Derby</td>
<td>Central Coast (CA)</td>
<td>Womens</td>
<td>.48564</td>
</tr>
<tr>
<td><b>361</b></td>
<td>417</td>
<td>Sioux City Roller Dames</td>
<td>Sioux City</td>
<td>Womens</td>
<td>.48511</td>
</tr>
<tr>
<td><b>362</b></td>
<td>418</td>
<td>Bandettes</td>
<td>San Diego Starlettes</td>
<td>Womens</td>
<td>.48497</td>
</tr>
<tr>
<td><b>363</b></td>
<td>419</td>
<td>Okanagan Roller Derby</td>
<td>Okanagan</td>
<td>Womens</td>
<td>.48462</td>
</tr>
<tr>
<td><b>364</b></td>
<td>420</td>
<td>Dark River Derby Coalition</td>
<td>Dark River</td>
<td>Womens</td>
<td>.48410</td>
</tr>
<tr>
<td><b>365</b></td>
<td>421</td>
<td>Hallam Hellcats Roller Derby</td>
<td>Hallam</td>
<td>Womens</td>
<td>.48397</td>
</tr>
<tr>
<td><b>366</b></td>
<td>422</td>
<td>Snake Pit Derby Dames</td>
<td>Snake Pit</td>
<td>Womens</td>
<td>.48378</td>
</tr>
<tr>
<td><b>367</b></td>
<td>423</td>
<td>Mass Attack Roller Derby</td>
<td>Mass Attack</td>
<td>Womens</td>
<td>.48369</td>
</tr>
<tr>
<td><b>368</b></td>
<td>424</td>
<td>Jane Deere</td>
<td>Calgary</td>
<td>Womens</td>
<td>.48342</td>
</tr>
<tr>
<td><b>369</b></td>
<td>425</td>
<td>Peach State Roller Derby</td>
<td>Peach State</td>
<td>Womens</td>
<td>.48310</td>
</tr>
<tr>
<td><b>370</b></td>
<td>426</td>
<td>Oxford Roller Derby</td>
<td>Oxford</td>
<td>Womens</td>
<td>.48285</td>
</tr>
<tr>
<td><b>371</b></td>
<td>427</td>
<td>South Side Derby Dolls</td>
<td>South Side (NSW)</td>
<td>Womens</td>
<td>.48253</td>
</tr>
<tr>
<td><b>372</b></td>
<td>428</td>
<td>Bellingham Roller Betties</td>
<td>Bellingham</td>
<td>Womens</td>
<td>.48251</td>
</tr>
<tr>
<td><b>373</b></td>
<td>429</td>
<td>Convict City Roller Derby</td>
<td>Convict City</td>
<td>Womens</td>
<td>.48181</td>
</tr>
<tr>
<td><b>374</b></td>
<td>430</td>
<td>Rated PG Rollergirls</td>
<td>Northstar</td>
<td>Womens</td>
<td>.48128</td>
</tr>
<tr>
<td><b>375</b></td>
<td>431</td>
<td>Bombshells</td>
<td>Boulder County</td>
<td>Womens</td>
<td>.48122</td>
</tr>
<tr>
<td><b>376</b></td>
<td>432</td>
<td>Alamo City Rollergirls</td>
<td>Alamo City</td>
<td>Womens</td>
<td>.48103</td>
</tr>
<tr>
<td><b>377</b></td>
<td>433</td>
<td>Harbour City Rollers</td>
<td>Harbour City Rollers</td>
<td>Womens</td>
<td>.48091</td>
</tr>
<tr>
<td><b>378</b></td>
<td>434</td>
<td>Road Ragers</td>
<td>Angel City</td>
<td>Womens</td>
<td>.48030</td>
</tr>
<tr>
<td><b>379</b></td>
<td>435</td>
<td>Battlestars</td>
<td>Brewcity</td>
<td>Womens</td>
<td>.48029</td>
</tr>
<tr>
<td><b>380</b></td>
<td>436</td>
<td>Rebellion Roller Derby</td>
<td>Rebellion</td>
<td>Womens</td>
<td>.47946</td>
</tr>
<tr>
<td><b>381</b></td>
<td>437</td>
<td>South Okanagan Roller Derby</td>
<td>Pistoleras</td>
<td>Womens</td>
<td>.47922</td>
</tr>
<tr>
<td><b>382</b></td>
<td>438</td>
<td>Roller Derby Panthers</td>
<td>Panthers Graou</td>
<td>Womens</td>
<td>.47894</td>
</tr>
<tr>
<td><b>383</b></td>
<td>439</td>
<td>Oxford Roller Derby B Team</td>
<td>Oxford</td>
<td>Womens</td>
<td>.47793</td>
</tr>
<tr>
<td><b>384</b></td>
<td>440</td>
<td>VCBs</td>
<td>Canberra</td>
<td>Womens</td>
<td>.47762</td>
</tr>
<tr>
<td><b>385</b></td>
<td>441</td>
<td>Sea Sirens</td>
<td>Tampa</td>
<td>Womens</td>
<td>.47759</td>
</tr>
<tr>
<td><b>386</b></td>
<td>442</td>
<td>Marseille Roller Derby Club (Women's)</td>
<td>Marseille</td>
<td>Womens</td>
<td>.47731</td>
</tr>
<tr>
<td><b>387</b></td>
<td>444</td>
<td>Brick City Bruisers</td>
<td>Garden State</td>
<td>Womens</td>
<td>.47712</td>
</tr>
<tr>
<td><b>388</b></td>
<td>445</td>
<td>Red Bluff Derby Girls</td>
<td>Red Bluff</td>
<td>Womens</td>
<td>.47680</td>
</tr>
<tr>
<td><b>389</b></td>
<td>446</td>
<td>River City Rollergirls</td>
<td>River City</td>
<td>Womens</td>
<td>.47616</td>
</tr>
<tr>
<td><b>390</b></td>
<td>447</td>
<td>Roller Derby Liège (Women's)</td>
<td>Liège (W)</td>
<td>Womens</td>
<td>.47609</td>
</tr>
<tr>
<td><b>391</b></td>
<td>449</td>
<td>Western Mass Destruction</td>
<td>Western Mass Destruction</td>
<td>Womens</td>
<td>.47571</td>
</tr>
<tr>
<td><b>392</b></td>
<td>450</td>
<td>Forest City Derby Girls</td>
<td>Forest City</td>
<td>Womens</td>
<td>.47562</td>
</tr>
<tr>
<td><b>393</b></td>
<td>451</td>
<td>Snake Pit Derby Dames</td>
<td>Snake Pit</td>
<td>Womens</td>
<td>.47509</td>
</tr>
<tr>
<td><b>394</b></td>
<td>452</td>
<td>Kent Roller Girls</td>
<td>Kent</td>
<td>Womens</td>
<td>.47487</td>
</tr>
<tr>
<td><b>395</b></td>
<td>453</td>
<td>ClarksVillain RollerGirls</td>
<td>ClarksVillains</td>
<td>Womens</td>
<td>.47469</td>
</tr>
<tr>
<td><b>396</b></td>
<td>454</td>
<td>Dirt City Roller Rats</td>
<td>Dirt City</td>
<td>Womens</td>
<td>.47462</td>
</tr>
<tr>
<td><b>397</b></td>
<td>455</td>
<td>NEO Roller Derby</td>
<td>NEO</td>
<td>Womens</td>
<td>.47269</td>
</tr>
<tr>
<td><b>398</b></td>
<td>456</td>
<td>Dixie Derby Girls</td>
<td>Dixie</td>
<td>Womens</td>
<td>.47254</td>
</tr>
<tr>
<td><b>399</b></td>
<td>457</td>
<td>High Tide Derby</td>
<td>High Tide</td>
<td>Womens</td>
<td>.47199</td>
</tr>
<tr>
<td><b>400</b></td>
<td>458</td>
<td>Saskatoon Roller Derby League</td>
<td>Saskatoon</td>
<td>Womens</td>
<td>.47128</td>
</tr>
<tr>
<td><b>401</b></td>
<td>459</td>
<td>Bay Rollers Roller Derby</td>
<td>Bay Rollers</td>
<td>Womens</td>
<td>.47121</td>
</tr>
<tr>
<td><b>402</b></td>
<td>460</td>
<td>Pile O' Bones Derby Club</td>
<td>Sugar Skulls</td>
<td>Womens</td>
<td>.47093</td>
</tr>
<tr>
<td><b>403</b></td>
<td>461</td>
<td>Harpies Roller Derby Milano</td>
<td>Milano</td>
<td>Womens</td>
<td>.47029</td>
</tr>
<tr>
<td><b>404</b></td>
<td>462</td>
<td>Wasteland Derby Dames</td>
<td>Wasteland</td>
<td>Womens</td>
<td>.46959</td>
</tr>
<tr>
<td><b>405</b></td>
<td>463</td>
<td>Mackay City Roller Maidens</td>
<td>Mackay City</td>
<td>Womens</td>
<td>.46939</td>
</tr>
<tr>
<td><b>406</b></td>
<td>464</td>
<td>A'Salt Creek Roller Girls</td>
<td>A'Salt Creek</td>
<td>Womens</td>
<td>.46850</td>
</tr>
<tr>
<td><b>407</b></td>
<td>465</td>
<td>Battlefords Roller Derby League</td>
<td>Battlefords</td>
<td>Womens</td>
<td>.46835</td>
</tr>
<tr>
<td><b>408</b></td>
<td>466</td>
<td>Radeladies</td>
<td>Adeladies</td>
<td>Womens</td>
<td>.46797</td>
</tr>
<tr>
<td><b>409</b></td>
<td>467</td>
<td>Sheffield Steel Rollergirls</td>
<td>Sheffield</td>
<td>Womens</td>
<td>.46788</td>
</tr>
<tr>
<td><b>410</b></td>
<td>468</td>
<td>Twin State Derby</td>
<td>Upper Valley</td>
<td>Womens</td>
<td>.46708</td>
</tr>
<tr>
<td><b>411</b></td>
<td>469</td>
<td>Wine Town Rollers</td>
<td>Wine Town</td>
<td>Womens</td>
<td>.46694</td>
</tr>
<tr>
<td><b>412</b></td>
<td>470</td>
<td>Reef City Rollergirls</td>
<td>Reef City</td>
<td>Womens</td>
<td>.46663</td>
</tr>
<tr>
<td><b>413</b></td>
<td>471</td>
<td>Lilac City Roller Girls</td>
<td>Lilac City</td>
<td>Womens</td>
<td>.46645</td>
</tr>
<tr>
<td><b>414</b></td>
<td>472</td>
<td>Anchor City Rollers</td>
<td>Halifax</td>
<td>Womens</td>
<td>.46630</td>
</tr>
<tr>
<td><b>415</b></td>
<td>473</td>
<td>Strong Island Derby Revolution</td>
<td>Strong Island</td>
<td>Womens</td>
<td>.46608</td>
</tr>
<tr>
<td><b>416</b></td>
<td>474</td>
<td>Les Divines Machines</td>
<td>Nantes</td>
<td>Womens</td>
<td>.46597</td>
</tr>
<tr>
<td><b>417</b></td>
<td>475</td>
<td>The Damned</td>
<td>Undead Bettys</td>
<td>Womens</td>
<td>.46567</td>
</tr>
<tr>
<td><b>418</b></td>
<td>476</td>
<td>Fox Cities Roller Derby</td>
<td>Fox Cities</td>
<td>Womens</td>
<td>.46557</td>
</tr>
<tr>
<td><b>419</b></td>
<td>477</td>
<td>Neath Port Talbot Roller Derby</td>
<td>Neath</td>
<td>Womens</td>
<td>.46470</td>
</tr>
<tr>
<td><b>420</b></td>
<td>478</td>
<td>Shore Points Roller Derby</td>
<td>Shore Points</td>
<td>Womens</td>
<td>.46333</td>
</tr>
<tr>
<td><b>421</b></td>
<td>479</td>
<td>Grunge City Rollers</td>
<td>Grunge City Elite</td>
<td>Womens</td>
<td>.46333</td>
</tr>
<tr>
<td><b>422</b></td>
<td>480</td>
<td>Greater Toronto Area Rollergirls</td>
<td>GTARollergirls</td>
<td>Womens</td>
<td>.46331</td>
</tr>
<tr>
<td><b>423</b></td>
<td>481</td>
<td>Willamette Kidney Thieves</td>
<td>Willamette</td>
<td>Womens</td>
<td>.46289</td>
</tr>
<tr>
<td><b>424</b></td>
<td>482</td>
<td>Greensboro Roller Derby</td>
<td>Greensboro</td>
<td>Womens</td>
<td>.46268</td>
</tr>
<tr>
<td><b>425</b></td>
<td>483</td>
<td>Dutchland Derby Rollers</td>
<td>Dutchland</td>
<td>Womens</td>
<td>.46247</td>
</tr>
<tr>
<td><b>426</b></td>
<td>484</td>
<td>KillaBytes</td>
<td>Silicon Valley</td>
<td>Womens</td>
<td>.46244</td>
</tr>
<tr>
<td><b>427</b></td>
<td>485</td>
<td>Rolling Hills Derby Dames</td>
<td>Rolling Hills</td>
<td>Womens</td>
<td>.46227</td>
</tr>
<tr>
<td><b>428</b></td>
<td>486</td>
<td>Roller Derby Metz Club</td>
<td>Metz</td>
<td>Womens</td>
<td>.46206</td>
</tr>
<tr>
<td><b>429</b></td>
<td>487</td>
<td>Dolly Rockit Rollers</td>
<td>Dolly Rockit</td>
<td>Womens</td>
<td>.46197</td>
</tr>
<tr>
<td><b>430</b></td>
<td>488</td>
<td>Cedar Valley Roller Derby</td>
<td>Cedar Valley</td>
<td>Womens</td>
<td>.46145</td>
</tr>
<tr>
<td><b>431</b></td>
<td>489</td>
<td>MOKAN Roller Girlz</td>
<td>MOKAN</td>
<td>Womens</td>
<td>.46143</td>
</tr>
<tr>
<td><b>432</b></td>
<td>490</td>
<td>Gang Green</td>
<td>Ohio</td>
<td>Womens</td>
<td>.46052</td>
</tr>
<tr>
<td><b>433</b></td>
<td>491</td>
<td>BSTRDs</td>
<td>Stockholm</td>
<td>Womens</td>
<td>.46037</td>
</tr>
<tr>
<td><b>434</b></td>
<td>492</td>
<td>Palm Coast Roller Derby</td>
<td>Palm Coast</td>
<td>Womens</td>
<td>.46006</td>
</tr>
<tr>
<td><b>435</b></td>
<td>493</td>
<td>Capital City Rollers</td>
<td>Capital City</td>
<td>Womens</td>
<td>.45999</td>
</tr>
<tr>
<td><b>436</b></td>
<td>494</td>
<td>Belfast Roller Derby</td>
<td>Belfast</td>
<td>Womens</td>
<td>.45907</td>
</tr>
<tr>
<td><b>437</b></td>
<td>495</td>
<td>NWO Roller Girls</td>
<td>NWO</td>
<td>Womens</td>
<td>.45883</td>
</tr>
<tr>
<td><b>438</b></td>
<td>496</td>
<td>Rum Rollers</td>
<td>Royal City</td>
<td>Womens</td>
<td>.45853</td>
</tr>
<tr>
<td><b>439</b></td>
<td>497</td>
<td>Juneau Roller Girls</td>
<td>Juneau</td>
<td>Womens</td>
<td>.45823</td>
</tr>
<tr>
<td><b>440</b></td>
<td>498</td>
<td>Tragic City Rollers</td>
<td>Tragic City</td>
<td>Womens</td>
<td>.45782</td>
</tr>
<tr>
<td><b>441</b></td>
<td>499</td>
<td>Hartford Area Roller Derby</td>
<td>Hartford Area</td>
<td>Womens</td>
<td>.45764</td>
</tr>
<tr>
<td><b>442</b></td>
<td>500</td>
<td>Cornwall Roller Derby</td>
<td>Cornwall</td>
<td>Womens</td>
<td>.45721</td>
</tr>
<tr>
<td><b>443</b></td>
<td>501</td>
<td>Hulls Angels Roller Dames</td>
<td>Hulls Angels</td>
<td>Womens</td>
<td>.45677</td>
</tr>
<tr>
<td><b>444</b></td>
<td>502</td>
<td>Swamp City Roller Rats</td>
<td>Swamp City</td>
<td>Womens</td>
<td>.45624</td>
</tr>
<tr>
<td><b>445</b></td>
<td>503</td>
<td>Les Sales Gosses</td>
<td>Sales Gosses</td>
<td>Womens</td>
<td>.45601</td>
</tr>
<tr>
<td><b>446</b></td>
<td>504</td>
<td>Munich Rolling Rebels</td>
<td>Munich</td>
<td>Womens</td>
<td>.45568</td>
</tr>
<tr>
<td><b>447</b></td>
<td>505</td>
<td>Wine Country Homewreckers</td>
<td>Sonoma</td>
<td>Womens</td>
<td>.45522</td>
</tr>
<tr>
<td><b>448</b></td>
<td>506</td>
<td>Killjoys</td>
<td>Killjoys</td>
<td>Womens</td>
<td>.45519</td>
</tr>
<tr>
<td><b>449</b></td>
<td>507</td>
<td>Ingles de Acero B</td>
<td>Barcelona</td>
<td>Womens</td>
<td>.45517</td>
</tr>
<tr>
<td><b>450</b></td>
<td>508</td>
<td>Grande Prairie Roller Derby</td>
<td>Grande Prairie</td>
<td>Womens</td>
<td>.45460</td>
</tr>
<tr>
<td><b>451</b></td>
<td>509</td>
<td>Steel Beamers</td>
<td>Steel City</td>
<td>Womens</td>
<td>.45417</td>
</tr>
<tr>
<td><b>452</b></td>
<td>510</td>
<td>Iron Range Maidens</td>
<td>Iron Range</td>
<td>Womens</td>
<td>.45381</td>
</tr>
<tr>
<td><b>453</b></td>
<td>511</td>
<td>Violent Lambs</td>
<td>Cincinnati</td>
<td>Womens</td>
<td>.45379</td>
</tr>
<tr>
<td><b>454</b></td>
<td>512</td>
<td>Rawlins Pen-Up Girlz</td>
<td>Rawlins</td>
<td>Womens</td>
<td>.45300</td>
</tr>
<tr>
<td><b>455</b></td>
<td>513</td>
<td>Palouse River Rampage</td>
<td>Palouse</td>
<td>Womens</td>
<td>.45290</td>
</tr>
<tr>
<td><b>456</b></td>
<td>514</td>
<td>Rubber City Rollergirls</td>
<td>Rubber City</td>
<td>Womens</td>
<td>.45271</td>
</tr>
<tr>
<td><b>457</b></td>
<td>515</td>
<td>Magic City Rollers B Team</td>
<td>Magic City Rollers</td>
<td>Womens</td>
<td>.45260</td>
</tr>
<tr>
<td><b>458</b></td>
<td>516</td>
<td>Bombshell Brawlers</td>
<td>Winnipeg</td>
<td>Womens</td>
<td>.45233</td>
</tr>
<tr>
<td><b>459</b></td>
<td>517</td>
<td>Muscogee Roller Girls</td>
<td>Muscogee</td>
<td>Womens</td>
<td>.45169</td>
</tr>
<tr>
<td><b>460</b></td>
<td>518</td>
<td>Resurrection Roller Girls</td>
<td>Resurrection</td>
<td>Womens</td>
<td>.45102</td>
</tr>
<tr>
<td><b>461</b></td>
<td>519</td>
<td>Norfolk Roller Derby</td>
<td>Norfolk</td>
<td>Womens</td>
<td>.45060</td>
</tr>
<tr>
<td><b>462</b></td>
<td>520</td>
<td>Cannie Gingers</td>
<td>Glasgow</td>
<td>Womens</td>
<td>.45048</td>
</tr>
<tr>
<td><b>463</b></td>
<td>521</td>
<td>Oil City Derby Girls</td>
<td>Oil City</td>
<td>Womens</td>
<td>.45039</td>
</tr>
<tr>
<td><b>464</b></td>
<td>522</td>
<td>Jukes of Hazzard</td>
<td>Atlanta</td>
<td>Womens</td>
<td>.45018</td>
</tr>
<tr>
<td><b>465</b></td>
<td>523</td>
<td>Hard Knox Roller Girls</td>
<td>Hard Knox</td>
<td>Womens</td>
<td>.45009</td>
</tr>
<tr>
<td><b>466</b></td>
<td>524</td>
<td>Kokeshi Rollerdolls</td>
<td>Kokeshi Rollerdolls</td>
<td>Womens</td>
<td>.44997</td>
</tr>
<tr>
<td><b>467</b></td>
<td>525</td>
<td>Kings County Derby Queens</td>
<td>Hooligans</td>
<td>Womens</td>
<td>.44875</td>
</tr>
<tr>
<td><b>468</b></td>
<td>526</td>
<td>Capitol Offenders</td>
<td>DC</td>
<td>Womens</td>
<td>.44863</td>
</tr>
<tr>
<td><b>469</b></td>
<td>527</td>
<td>Gas City Roller Derby Association (Women)</td>
<td>Gas City</td>
<td>Womens</td>
<td>.44795</td>
</tr>
<tr>
<td><b>470</b></td>
<td>528</td>
<td>National Maulers</td>
<td>DC</td>
<td>Womens</td>
<td>.44784</td>
</tr>
<tr>
<td><b>471</b></td>
<td>529</td>
<td>Prairieland Punishers Roller Derby</td>
<td>Punishers</td>
<td>Womens</td>
<td>.44744</td>
</tr>
<tr>
<td><b>472</b></td>
<td>530</td>
<td>Music City Brawl Stars</td>
<td>Nashville</td>
<td>Womens</td>
<td>.44716</td>
</tr>
<tr>
<td><b>473</b></td>
<td>531</td>
<td>Suburbia Roller Derby</td>
<td>Suburbia</td>
<td>Womens</td>
<td>.44708</td>
</tr>
<tr>
<td><b>474</b></td>
<td>532</td>
<td>Star City Roller Girls</td>
<td>Star City</td>
<td>Womens</td>
<td>.44698</td>
</tr>
<tr>
<td><b>475</b></td>
<td>533</td>
<td>Smokin' Laces</td>
<td>Mainland Misfits</td>
<td>Womens</td>
<td>.44692</td>
</tr>
<tr>
<td><b>476</b></td>
<td>535</td>
<td>Gas City Rollers</td>
<td>Gas City</td>
<td>Womens</td>
<td>.44615</td>
</tr>
<tr>
<td><b>477</b></td>
<td>536</td>
<td>Cologne Roller Derby</td>
<td>Cologne</td>
<td>Womens</td>
<td>.44560</td>
</tr>
<tr>
<td><b>478</b></td>
<td>537</td>
<td>Gold Pain City Derby Girls</td>
<td>Gold Pain</td>
<td>Womens</td>
<td>.44519</td>
</tr>
<tr>
<td><b>479</b></td>
<td>538</td>
<td>Continental Dividers</td>
<td>Ark Valley</td>
<td>Womens</td>
<td>.44518</td>
</tr>
<tr>
<td><b>480</b></td>
<td>539</td>
<td>Whip-Its</td>
<td>Leeds</td>
<td>Womens</td>
<td>.44515</td>
</tr>
<tr>
<td><b>481</b></td>
<td>540</td>
<td>Aftershocks</td>
<td>Peninsula</td>
<td>Womens</td>
<td>.44488</td>
</tr>
<tr>
<td><b>482</b></td>
<td>541</td>
<td>Central Ohio Roller Derby</td>
<td>Central Ohio</td>
<td>Womens</td>
<td>.44414</td>
</tr>
<tr>
<td><b>483</b></td>
<td>542</td>
<td>Peninsula Roller Girls</td>
<td>Peninsula</td>
<td>Womens</td>
<td>.44407</td>
</tr>
<tr>
<td><b>484</b></td>
<td>543</td>
<td>Slamazons</td>
<td>Pikes Peak</td>
<td>Womens</td>
<td>.44376</td>
</tr>
<tr>
<td><b>485</b></td>
<td>544</td>
<td>CoMo Derby Dames</td>
<td>CoMo</td>
<td>Womens</td>
<td>.44346</td>
</tr>
<tr>
<td><b>486</b></td>
<td>545</td>
<td>Pacific Coast Recycled Rollers</td>
<td>Recycled Rollers</td>
<td>Womens</td>
<td>.44281</td>
</tr>
<tr>
<td><b>487</b></td>
<td>546</td>
<td>Joint Base Lewis-McChord Bettie Brigade</td>
<td>Bettie Brigade</td>
<td>Womens</td>
<td>.44280</td>
</tr>
<tr>
<td><b>488</b></td>
<td>547</td>
<td>Hertfordshire Roller Derby</td>
<td>Hell's Belles</td>
<td>Womens</td>
<td>.44225</td>
</tr>
<tr>
<td><b>489</b></td>
<td>548</td>
<td>Killer Rollbots</td>
<td>Rollbots</td>
<td>Womens</td>
<td>.44216</td>
</tr>
<tr>
<td><b>490</b></td>
<td>549</td>
<td>Capital City Crushers</td>
<td>Crushers</td>
<td>Womens</td>
<td>.44214</td>
</tr>
<tr>
<td><b>491</b></td>
<td>550</td>
<td>Richland County Regulators Derby Team</td>
<td>Richland County Regulators</td>
<td>Womens</td>
<td>.44201</td>
</tr>
<tr>
<td><b>492</b></td>
<td>551</td>
<td>Tokyo Roller Girls</td>
<td>Tokyo</td>
<td>Womens</td>
<td>.44184</td>
</tr>
<tr>
<td><b>493</b></td>
<td>552</td>
<td>Borderland Brawlers Roller Derby</td>
<td>Borderland Brawlers</td>
<td>Womens</td>
<td>.44159</td>
</tr>
<tr>
<td><b>494</b></td>
<td>553</td>
<td>Roller Girls of the Apocalypse</td>
<td>RGA The Wreckoning</td>
<td>Womens</td>
<td>.44126</td>
</tr>
<tr>
<td><b>495</b></td>
<td>554</td>
<td>Portneuf Valley Bruisers</td>
<td>Portneuf</td>
<td>Womens</td>
<td>.44098</td>
</tr>
<tr>
<td><b>496</b></td>
<td>555</td>
<td>Kouvola Rock N Rollers</td>
<td>Kouvola</td>
<td>Womens</td>
<td>.44069</td>
</tr>
<tr>
<td><b>497</b></td>
<td>556</td>
<td>Sunshine Coast Roller Girls</td>
<td>Sunshine Coast</td>
<td>Womens</td>
<td>.44055</td>
</tr>
<tr>
<td><b>498</b></td>
<td>557</td>
<td>Storm City Roller Girls</td>
<td>Storm City</td>
<td>Womens</td>
<td>.43993</td>
</tr>
<tr>
<td><b>499</b></td>
<td>558</td>
<td>Prague City Roller Derby</td>
<td>Prague</td>
<td>Womens</td>
<td>.43985</td>
</tr>
<tr>
<td><b>500</b></td>
<td>559</td>
<td>Hell's Ass Derby Girls</td>
<td>Strasbourg</td>
<td>Womens</td>
<td>.43942</td>
</tr>
<tr>
<td><b>501</b></td>
<td>560</td>
<td>Blitz</td>
<td>Dutchland</td>
<td>Womens</td>
<td>.43928</td>
</tr>
<tr>
<td><b>502</b></td>
<td>561</td>
<td>Heartland Hellcats</td>
<td>N. Platte</td>
<td>Womens</td>
<td>.43859</td>
</tr>
<tr>
<td><b>503</b></td>
<td>562</td>
<td>Living Dead</td>
<td>E-Ville</td>
<td>Womens</td>
<td>.43852</td>
</tr>
<tr>
<td><b>504</b></td>
<td>563</td>
<td>Jersey Shore Roller Girls</td>
<td>Jersey Shore</td>
<td>Womens</td>
<td>.43810</td>
</tr>
<tr>
<td><b>505</b></td>
<td>564</td>
<td>New Hampshire Roller Derby</td>
<td>New Hampshire</td>
<td>Womens</td>
<td>.43808</td>
</tr>
<tr>
<td><b>506</b></td>
<td>565</td>
<td>Bellingham FLASH</td>
<td>Bellingham</td>
<td>Womens</td>
<td>.43743</td>
</tr>
<tr>
<td><b>507</b></td>
<td>566</td>
<td>Roller Derby Twente</td>
<td>Twente</td>
<td>Womens</td>
<td>.43734</td>
</tr>
<tr>
<td><b>508</b></td>
<td>567</td>
<td>Northwest Derby Company</td>
<td>Northwest</td>
<td>Womens</td>
<td>.43651</td>
</tr>
<tr>
<td><b>509</b></td>
<td>568</td>
<td>Kingston City Rollers</td>
<td>Kingston City</td>
<td>Womens</td>
<td>.43631</td>
</tr>
<tr>
<td><b>510</b></td>
<td>569</td>
<td>Fight Hawks</td>
<td>Granite City</td>
<td>Womens</td>
<td>.43606</td>
</tr>
<tr>
<td><b>511</b></td>
<td>570</td>
<td>The Anguanas Roller Derby Vicenza</td>
<td>Anguanas</td>
<td>Womens</td>
<td>.43571</td>
</tr>
<tr>
<td><b>512</b></td>
<td>571</td>
<td>Big Sky All Stars</td>
<td>Big Sky</td>
<td>Womens</td>
<td>.43491</td>
</tr>
<tr>
<td><b>513</b></td>
<td>572</td>
<td>Bembel Town Rollergirls</td>
<td>Bembeltown</td>
<td>Womens</td>
<td>.43438</td>
</tr>
<tr>
<td><b>514</b></td>
<td>573</td>
<td>Nottingham Roller Girls</td>
<td>Nottingham</td>
<td>Womens</td>
<td>.43424</td>
</tr>
<tr>
<td><b>515</b></td>
<td>574</td>
<td>Barockcity Rollerderby</td>
<td>Barockcity</td>
<td>Womens</td>
<td>.43424</td>
</tr>
<tr>
<td><b>516</b></td>
<td>575</td>
<td>Aarhus Derby Danes</td>
<td>Aarhus</td>
<td>Womens</td>
<td>.43314</td>
</tr>
<tr>
<td><b>517</b></td>
<td>576</td>
<td>Subzero Sirens</td>
<td>Queen City</td>
<td>Womens</td>
<td>.43236</td>
</tr>
<tr>
<td><b>518</b></td>
<td>577</td>
<td>Lyon Association Roller Derby</td>
<td>Lyonnaises</td>
<td>Womens</td>
<td>.43222</td>
</tr>
<tr>
<td><b>519</b></td>
<td>578</td>
<td>Reading Derby Girls</td>
<td>Reading</td>
<td>Womens</td>
<td>.43195</td>
</tr>
<tr>
<td><b>520</b></td>
<td>579</td>
<td>New Jersey Roller Derby</td>
<td>Morristown: NJRD</td>
<td>Womens</td>
<td>.43162</td>
</tr>
<tr>
<td><b>521</b></td>
<td>580</td>
<td>Savannah Derby Devils</td>
<td>Savannah</td>
<td>Womens</td>
<td>.43129</td>
</tr>
<tr>
<td><b>522</b></td>
<td>581</td>
<td>Coachella Valley Derby Girls</td>
<td>Coachella Valley</td>
<td>Womens</td>
<td>.43110</td>
</tr>
<tr>
<td><b>523</b></td>
<td>582</td>
<td>Ring City Rollergirls</td>
<td>Ring City</td>
<td>Womens</td>
<td>.43105</td>
</tr>
<tr>
<td><b>524</b></td>
<td>583</td>
<td>Hellions of Troy Roller Derby</td>
<td>Hellions</td>
<td>Womens</td>
<td>.43041</td>
</tr>
<tr>
<td><b>525</b></td>
<td>584</td>
<td>Roller Derby Belfort</td>
<td>Belfort</td>
<td>Womens</td>
<td>.43038</td>
</tr>
<tr>
<td><b>526</b></td>
<td>585</td>
<td>580 Rollergirls</td>
<td>580</td>
<td>Womens</td>
<td>.43037</td>
</tr>
<tr>
<td><b>527</b></td>
<td>586</td>
<td>El Paso Roller Derby</td>
<td>El Paso</td>
<td>Womens</td>
<td>.43028</td>
</tr>
<tr>
<td><b>528</b></td>
<td>587</td>
<td>Killah Beez</td>
<td>Providence</td>
<td>Womens</td>
<td>.42959</td>
</tr>
<tr>
<td><b>529</b></td>
<td>588</td>
<td>Audio Assault</td>
<td>NEO</td>
<td>Womens</td>
<td>.42940</td>
</tr>
<tr>
<td><b>530</b></td>
<td>589</td>
<td>The Parliament of Pain</td>
<td>The Parliament of Pain</td>
<td>Womens</td>
<td>.42938</td>
</tr>
<tr>
<td><b>531</b></td>
<td>590</td>
<td>Hazmat Crew</td>
<td>Burning River</td>
<td>Womens</td>
<td>.42904</td>
</tr>
<tr>
<td><b>532</b></td>
<td>591</td>
<td>Club Roller Derby 38</td>
<td>Marmots</td>
<td>Womens</td>
<td>.42868</td>
</tr>
<tr>
<td><b>533</b></td>
<td>592</td>
<td>Valkyrias Roller Derby</td>
<td>Valkyrias</td>
<td>Womens</td>
<td>.42861</td>
</tr>
<tr>
<td><b>534</b></td>
<td>593</td>
<td>Project Mayhem</td>
<td>Rocky Mtn.</td>
<td>Womens</td>
<td>.42855</td>
</tr>
<tr>
<td><b>535</b></td>
<td>594</td>
<td>Bangor Roller Derby B-Team</td>
<td>Bangor</td>
<td>Womens</td>
<td>.42839</td>
</tr>
<tr>
<td><b>536</b></td>
<td>595</td>
<td>Wreckin' Roller Rebels</td>
<td>Wreckin' Rebels</td>
<td>Womens</td>
<td>.42828</td>
</tr>
<tr>
<td><b>537</b></td>
<td>596</td>
<td>Västerås Roller Derby</td>
<td>Västerås</td>
<td>Womens</td>
<td>.42803</td>
</tr>
<tr>
<td><b>538</b></td>
<td>597</td>
<td>Mad Hitters</td>
<td>Muddy River</td>
<td>Womens</td>
<td>.42791</td>
</tr>
<tr>
<td><b>539</b></td>
<td>598</td>
<td>Echo City Knockouts</td>
<td>Echo City</td>
<td>Womens</td>
<td>.42787</td>
</tr>
<tr>
<td><b>540</b></td>
<td>599</td>
<td>Black Harrts</td>
<td>Cape Fear</td>
<td>Womens</td>
<td>.42756</td>
</tr>
<tr>
<td><b>541</b></td>
<td>600</td>
<td>Diamond Valley Roller Derby Club</td>
<td>Diamond Valley</td>
<td>Womens</td>
<td>.42699</td>
</tr>
<tr>
<td><b>542</b></td>
<td>601</td>
<td>The Cubs</td>
<td>Gent Go Go</td>
<td>Womens</td>
<td>.42690</td>
</tr>
<tr>
<td><b>543</b></td>
<td>602</td>
<td>West Coast Derby Knockouts</td>
<td>West Coast Knockouts</td>
<td>Womens</td>
<td>.42610</td>
</tr>
<tr>
<td><b>544</b></td>
<td>603</td>
<td>Brick House Betties</td>
<td>Brick House Betties</td>
<td>Womens</td>
<td>.42606</td>
</tr>
<tr>
<td><b>545</b></td>
<td>604</td>
<td>Fierce Valley Roller Girls</td>
<td>Fierce Valley</td>
<td>Womens</td>
<td>.42601</td>
</tr>
<tr>
<td><b>546</b></td>
<td>605</td>
<td>Devil Dog Derby Dames</td>
<td>Devil Dog Derby</td>
<td>Womens</td>
<td>.42598</td>
</tr>
<tr>
<td><b>547</b></td>
<td>606</td>
<td>SWAT team</td>
<td>Ft. Wayne</td>
<td>Womens</td>
<td>.42589</td>
</tr>
<tr>
<td><b>548</b></td>
<td>607</td>
<td>Boom Town Derby Dames</td>
<td>Boom Town</td>
<td>Womens</td>
<td>.42576</td>
</tr>
<tr>
<td><b>549</b></td>
<td>608</td>
<td>Juggernaughties</td>
<td>Duke</td>
<td>Womens</td>
<td>.42556</td>
</tr>
<tr>
<td><b>550</b></td>
<td>609</td>
<td>Lightning</td>
<td>Paradise City</td>
<td>Womens</td>
<td>.42524</td>
</tr>
<tr>
<td><b>551</b></td>
<td>610</td>
<td>Westside Wreck Hers Roller Derby</td>
<td>Wreck Hers</td>
<td>Womens</td>
<td>.42471</td>
</tr>
<tr>
<td><b>552</b></td>
<td>611</td>
<td>Ballarat Roller Derby League</td>
<td>Ballarat</td>
<td>Womens</td>
<td>.42463</td>
</tr>
<tr>
<td><b>553</b></td>
<td>612</td>
<td>Harrisburg Area Roller Derby</td>
<td>Harrisburg</td>
<td>Womens</td>
<td>.42411</td>
</tr>
<tr>
<td><b>554</b></td>
<td>613</td>
<td>Black-n-Bluegrass RollerGirls</td>
<td>Black-n-Bluegrass</td>
<td>Womens</td>
<td>.42364</td>
</tr>
<tr>
<td><b>555</b></td>
<td>614</td>
<td>Maiden Grrders</td>
<td>Glasgow</td>
<td>Womens</td>
<td>.42275</td>
</tr>
<tr>
<td><b>556</b></td>
<td>615</td>
<td>BisMan Roller Derby (Women's)</td>
<td>Bombshellz</td>
<td>Womens</td>
<td>.42233</td>
</tr>
<tr>
<td><b>557</b></td>
<td>616</td>
<td>Hidden City Derby Girls</td>
<td>Hidden City</td>
<td>Womens</td>
<td>.42213</td>
</tr>
<tr>
<td><b>558</b></td>
<td>617</td>
<td>Glorious Batardes</td>
<td>Lille</td>
<td>Womens</td>
<td>.42174</td>
</tr>
<tr>
<td><b>559</b></td>
<td>618</td>
<td>Fargo Moorhead Derby Girls</td>
<td>Fargo Moorhead</td>
<td>Womens</td>
<td>.42164</td>
</tr>
<tr>
<td><b>560</b></td>
<td>619</td>
<td>South West Sask Roller Derby Association</td>
<td>Redneck Betties</td>
<td>Womens</td>
<td>.42153</td>
</tr>
<tr>
<td><b>561</b></td>
<td>620</td>
<td>Thunder City Derby Sirens</td>
<td>Thunder City</td>
<td>Womens</td>
<td>.42140</td>
</tr>
<tr>
<td><b>562</b></td>
<td>621</td>
<td>Carson Victory Rollers</td>
<td>Carson</td>
<td>Womens</td>
<td>.42128</td>
</tr>
<tr>
<td><b>563</b></td>
<td>622</td>
<td>Ohio Valley Roller Girls</td>
<td>Ohio Valley</td>
<td>Womens</td>
<td>.42116</td>
</tr>
<tr>
<td><b>564</b></td>
<td>623</td>
<td>Two Rivers Roller Derby</td>
<td>Two Rivers</td>
<td>Womens</td>
<td>.42094</td>
</tr>
<tr>
<td><b>565</b></td>
<td>624</td>
<td>Bay City Rollers</td>
<td>Bay City</td>
<td>Womens</td>
<td>.42076</td>
</tr>
<tr>
<td><b>566</b></td>
<td>625</td>
<td>Outlaws Roller Derby</td>
<td>Outlaws Roller Derby</td>
<td>Womens</td>
<td>.42055</td>
</tr>
<tr>
<td><b>567</b></td>
<td>626</td>
<td>Milton Keynes Roller Derby</td>
<td>Milton Keynes</td>
<td>Womens</td>
<td>.42030</td>
</tr>
<tr>
<td><b>568</b></td>
<td>627</td>
<td>Thunder Bay Roller Derby</td>
<td>Thunder Bay</td>
<td>Womens</td>
<td>.42021</td>
</tr>
<tr>
<td><b>569</b></td>
<td>628</td>
<td>Breakwater Blackhearts</td>
<td>Rock Coast</td>
<td>Womens</td>
<td>.41958</td>
</tr>
<tr>
<td><b>570</b></td>
<td>629</td>
<td>East Side Wheelers</td>
<td>East Side Wheelers</td>
<td>Womens</td>
<td>.41932</td>
</tr>
<tr>
<td><b>571</b></td>
<td>630</td>
<td>Belmont Bruisers</td>
<td>Charlottesville</td>
<td>Womens</td>
<td>.41895</td>
</tr>
<tr>
<td><b>572</b></td>
<td>631</td>
<td>Circle City Derby Girls</td>
<td>Circle City</td>
<td>Womens</td>
<td>.41891</td>
</tr>
<tr>
<td><b>573</b></td>
<td>632</td>
<td>Twisted Sisters (BCR)</td>
<td>Bay City</td>
<td>Womens</td>
<td>.41806</td>
</tr>
<tr>
<td><b>574</b></td>
<td>633</td>
<td>Soul City Sirens</td>
<td>Soul City</td>
<td>Womens</td>
<td>.41786</td>
</tr>
<tr>
<td><b>575</b></td>
<td>634</td>
<td>Female Trouble</td>
<td>Charm City</td>
<td>Womens</td>
<td>.41714</td>
</tr>
<tr>
<td><b>576</b></td>
<td>635</td>
<td>Dakota City Demolition Crew</td>
<td>Dakota City</td>
<td>Womens</td>
<td>.41705</td>
</tr>
<tr>
<td><b>577</b></td>
<td>636</td>
<td>Toowoomba City Rollers</td>
<td>Toowoomba</td>
<td>Womens</td>
<td>.41684</td>
</tr>
<tr>
<td><b>578</b></td>
<td>637</td>
<td>Black Diamond Rollers</td>
<td>Black Diamond</td>
<td>Womens</td>
<td>.41646</td>
</tr>
<tr>
<td><b>579</b></td>
<td>638</td>
<td>Wonder Brawlers</td>
<td>Central NY</td>
<td>Womens</td>
<td>.41599</td>
</tr>
<tr>
<td><b>580</b></td>
<td>639</td>
<td>Central Arkansas Roller Derby</td>
<td>Central Arkansas</td>
<td>Womens</td>
<td>.41599</td>
</tr>
<tr>
<td><b>581</b></td>
<td>640</td>
<td>Bourbon Brawlers</td>
<td>Derby City</td>
<td>Womens</td>
<td>.41581</td>
</tr>
<tr>
<td><b>582</b></td>
<td>641</td>
<td>Piritorin Ässät</td>
<td>Kallio</td>
<td>Womens</td>
<td>.41538</td>
</tr>
<tr>
<td><b>583</b></td>
<td>642</td>
<td>Albany All Stars Roller Derby</td>
<td>Albany</td>
<td>Womens</td>
<td>.41527</td>
</tr>
<tr>
<td><b>584</b></td>
<td>643</td>
<td>Dam City Rollers</td>
<td>Dam City</td>
<td>Womens</td>
<td>.41454</td>
</tr>
<tr>
<td><b>585</b></td>
<td>644</td>
<td>Suffolk Roller Derby (Women's)</td>
<td>Suffolk (Women's)</td>
<td>Womens</td>
<td>.41452</td>
</tr>
<tr>
<td><b>586</b></td>
<td>645</td>
<td>Durham Region Roller Derby</td>
<td>Durham (Canada)</td>
<td>Womens</td>
<td>.41439</td>
</tr>
<tr>
<td><b>587</b></td>
<td>647</td>
<td>Beloit Bombshells</td>
<td>Beloit Bombshells</td>
<td>Womens</td>
<td>.41339</td>
</tr>
<tr>
<td><b>588</b></td>
<td>648</td>
<td>Wiltshire Roller Derby</td>
<td>Wiltshire</td>
<td>Womens</td>
<td>.41327</td>
</tr>
<tr>
<td><b>589</b></td>
<td>649</td>
<td>Battalion of Skates</td>
<td>Ventura</td>
<td>Womens</td>
<td>.41291</td>
</tr>
<tr>
<td><b>590</b></td>
<td>650</td>
<td>Black Ice Brawlers</td>
<td>Green Mt.</td>
<td>Womens</td>
<td>.41261</td>
</tr>
<tr>
<td><b>591</b></td>
<td>651</td>
<td>Flint Roller Derby</td>
<td>Flint City</td>
<td>Womens</td>
<td>.41245</td>
</tr>
<tr>
<td><b>592</b></td>
<td>652</td>
<td>Shade Brigade</td>
<td>Chicago Outfit</td>
<td>Womens</td>
<td>.41243</td>
</tr>
<tr>
<td><b>593</b></td>
<td>653</td>
<td>Tweed Valley Rollers</td>
<td>Tweed Valley</td>
<td>Womens</td>
<td>.41240</td>
</tr>
<tr>
<td><b>594</b></td>
<td>654</td>
<td>State College Area Roller Derby</td>
<td>State College</td>
<td>Womens</td>
<td>.41211</td>
</tr>
<tr>
<td><b>595</b></td>
<td>655</td>
<td>Miss B-havers</td>
<td>Columbia</td>
<td>Womens</td>
<td>.41161</td>
</tr>
<tr>
<td><b>596</b></td>
<td>656</td>
<td>Lil Chicago Roller Derby</td>
<td>Lil Chicago</td>
<td>Womens</td>
<td>.41150</td>
</tr>
<tr>
<td><b>597</b></td>
<td>657</td>
<td>Compagnie Cruelle</td>
<td>Bordeaux</td>
<td>Womens</td>
<td>.41144</td>
</tr>
<tr>
<td><b>598</b></td>
<td>658</td>
<td>Enchanted Mountain Roller Derby</td>
<td>Enchanted Mountain</td>
<td>Womens</td>
<td>.41142</td>
</tr>
<tr>
<td><b>599</b></td>
<td>659</td>
<td>Renegade Derby Dames</td>
<td>Renegade</td>
<td>Womens</td>
<td>.41130</td>
</tr>
<tr>
<td><b>600</b></td>
<td>660</td>
<td>Spokannibals</td>
<td>Spokannibals</td>
<td>Womens</td>
<td>.41038</td>
</tr>
<tr>
<td><b>601</b></td>
<td>661</td>
<td>Mount Militia Derby Crew</td>
<td>Mount Militia</td>
<td>Womens</td>
<td>.41016</td>
</tr>
<tr>
<td><b>602</b></td>
<td>662</td>
<td>Wellington Roller Derby</td>
<td>Feims</td>
<td>Womens</td>
<td>.40962</td>
</tr>
<tr>
<td><b>603</b></td>
<td>663</td>
<td>Orange Crush</td>
<td>Rage City</td>
<td>Womens</td>
<td>.40960</td>
</tr>
<tr>
<td><b>604</b></td>
<td>664</td>
<td>Capital Corruption</td>
<td>Lansing Vixens</td>
<td>Womens</td>
<td>.40940</td>
</tr>
<tr>
<td><b>605</b></td>
<td>665</td>
<td>Albany B Team</td>
<td>Albany</td>
<td>Womens</td>
<td>.40924</td>
</tr>
<tr>
<td><b>606</b></td>
<td>666</td>
<td>Salina Sirens Roller Derby</td>
<td>Salina Sirens</td>
<td>Womens</td>
<td>.40920</td>
</tr>
<tr>
<td><b>607</b></td>
<td>667</td>
<td>Rainbow Furies</td>
<td>Toulouse</td>
<td>Womens</td>
<td>.40901</td>
</tr>
<tr>
<td><b>608</b></td>
<td>668</td>
<td>C-Stars</td>
<td>Stockholm</td>
<td>Womens</td>
<td>.40891</td>
</tr>
<tr>
<td><b>609</b></td>
<td>669</td>
<td>Bristol Roller Derby B</td>
<td>Bristol A</td>
<td>Womens</td>
<td>.40814</td>
</tr>
<tr>
<td><b>610</b></td>
<td>670</td>
<td>Sis-Q Rollerz</td>
<td>Sis-Q</td>
<td>Womens</td>
<td>.40812</td>
</tr>
<tr>
<td><b>611</b></td>
<td>671</td>
<td>Northland Nightmares Roller Girlz</td>
<td>Northland Nightmares</td>
<td>Womens</td>
<td>.40779</td>
</tr>
<tr>
<td><b>612</b></td>
<td>672</td>
<td>Port Macquarie Roller Derby</td>
<td>Port Macquarie</td>
<td>Womens</td>
<td>.40732</td>
</tr>
<tr>
<td><b>613</b></td>
<td>673</td>
<td>Rayo Dockers Roller Derby</td>
<td>Rayo Dockers</td>
<td>Womens</td>
<td>.40691</td>
</tr>
<tr>
<td><b>614</b></td>
<td>674</td>
<td>Seaside Siren Roller Girls</td>
<td>Seaside Sirens</td>
<td>Womens</td>
<td>.40664</td>
</tr>
<tr>
<td><b>615</b></td>
<td>676</td>
<td>Gainesville Roller Rebels</td>
<td>Gainesville</td>
<td>Womens</td>
<td>.40616</td>
</tr>
<tr>
<td><b>616</b></td>
<td>677</td>
<td>Jerzey Derby Brigade</td>
<td>Morristown: JDB</td>
<td>Womens</td>
<td>.40581</td>
</tr>
<tr>
<td><b>617</b></td>
<td>678</td>
<td>Sioux Falls Roller Dollz</td>
<td>Sioux Falls</td>
<td>Womens</td>
<td>.40562</td>
</tr>
<tr>
<td><b>618</b></td>
<td>679</td>
<td>Mississippi Valley Mayhem</td>
<td>Mississippi Valley</td>
<td>Womens</td>
<td>.40543</td>
</tr>
<tr>
<td><b>619</b></td>
<td>680</td>
<td>Orlando Psycho City Derby Girls</td>
<td>Psycho City</td>
<td>Womens</td>
<td>.40520</td>
</tr>
<tr>
<td><b>620</b></td>
<td>681</td>
<td>Nice Roller Derby</td>
<td>Nice</td>
<td>Womens</td>
<td>.40504</td>
</tr>
<tr>
<td><b>621</b></td>
<td>682</td>
<td>Motherlode Area Derby</td>
<td>MAD</td>
<td>Womens</td>
<td>.40437</td>
</tr>
<tr>
<td><b>622</b></td>
<td>683</td>
<td>Maui Rollergirls</td>
<td>Maui</td>
<td>Womens</td>
<td>.40420</td>
</tr>
<tr>
<td><b>623</b></td>
<td>684</td>
<td>Diamond District</td>
<td>Gotham</td>
<td>Womens</td>
<td>.40416</td>
</tr>
<tr>
<td><b>624</b></td>
<td>685</td>
<td>Glass City Rollers</td>
<td>Glass City</td>
<td>Womens</td>
<td>.40387</td>
</tr>
<tr>
<td><b>625</b></td>
<td>686</td>
<td>The B-Headers</td>
<td>Royal Windsor</td>
<td>Womens</td>
<td>.40383</td>
</tr>
<tr>
<td><b>626</b></td>
<td>687</td>
<td>Dead River Derby</td>
<td>Dead River</td>
<td>Womens</td>
<td>.40369</td>
</tr>
<tr>
<td><b>627</b></td>
<td>688</td>
<td>Dorset Roller Girls</td>
<td>Dorset</td>
<td>Womens</td>
<td>.40342</td>
</tr>
<tr>
<td><b>628</b></td>
<td>689</td>
<td>Tar Sand Betties</td>
<td>Tar Sand Betties</td>
<td>Womens</td>
<td>.40333</td>
</tr>
<tr>
<td><b>629</b></td>
<td>690</td>
<td>Badasses</td>
<td>Rockin' Rollers</td>
<td>Womens</td>
<td>.40287</td>
</tr>
<tr>
<td><b>630</b></td>
<td>691</td>
<td>Roller Underground</td>
<td>Roller Underground</td>
<td>Womens</td>
<td>.40283</td>
</tr>
<tr>
<td><b>631</b></td>
<td>692</td>
<td>Small Town Outlaws</td>
<td>Small Town</td>
<td>Womens</td>
<td>.40265</td>
</tr>
<tr>
<td><b>632</b></td>
<td>693</td>
<td>Grapes of Wrath</td>
<td>Wine Town</td>
<td>Womens</td>
<td>.40258</td>
</tr>
<tr>
<td><b>633</b></td>
<td>694</td>
<td>Central Coast Roller Derby United</td>
<td>Central Coast (NSW)</td>
<td>Womens</td>
<td>.40184</td>
</tr>
<tr>
<td><b>634</b></td>
<td>695</td>
<td>Brawlin' Broads</td>
<td>Bay State Brawlers</td>
<td>Womens</td>
<td>.40153</td>
</tr>
<tr>
<td><b>635</b></td>
<td>697</td>
<td>Roma Roller Derby</td>
<td>Roma</td>
<td>Womens</td>
<td>.40046</td>
</tr>
<tr>
<td><b>636</b></td>
<td>698</td>
<td>Mason-Dixon Roller Vixens</td>
<td>Mason-Dixon</td>
<td>Womens</td>
<td>.40012</td>
</tr>
<tr>
<td><b>637</b></td>
<td>699</td>
<td>Loco City Derby Girls</td>
<td>Loco City</td>
<td>Womens</td>
<td>.40007</td>
</tr>
<tr>
<td><b>638</b></td>
<td>700</td>
<td>Bootleg City Roller Derby</td>
<td>Moonshine Maidens</td>
<td>Womens</td>
<td>.40006</td>
</tr>
<tr>
<td><b>639</b></td>
<td>701</td>
<td>Destruction Dames</td>
<td>Demolition</td>
<td>Womens</td>
<td>.39980</td>
</tr>
<tr>
<td><b>640</b></td>
<td>702</td>
<td>West Texas Roller Dollz</td>
<td>West Texas</td>
<td>Womens</td>
<td>.39977</td>
</tr>
<tr>
<td><b>641</b></td>
<td>703</td>
<td>Preston Roller Girls</td>
<td>Preston</td>
<td>Womens</td>
<td>.39952</td>
</tr>
<tr>
<td><b>642</b></td>
<td>704</td>
<td>Hell's Belles</td>
<td>St. Chux</td>
<td>Womens</td>
<td>.39916</td>
</tr>
<tr>
<td><b>643</b></td>
<td>705</td>
<td>North Cs</td>
<td>Newcastle</td>
<td>Womens</td>
<td>.39819</td>
</tr>
<tr>
<td><b>644</b></td>
<td>706</td>
<td>Ume Radical Rollers</td>
<td>Ume</td>
<td>Womens</td>
<td>.39718</td>
</tr>
<tr>
<td><b>645</b></td>
<td>707</td>
<td>Cat 5’s</td>
<td>Gold Coast (FL)</td>
<td>Womens</td>
<td>.39717</td>
</tr>
<tr>
<td><b>646</b></td>
<td>708</td>
<td>Superior Sirens</td>
<td>Dead River</td>
<td>Womens</td>
<td>.39688</td>
</tr>
<tr>
<td><b>647</b></td>
<td>710</td>
<td>Roller Derby Alcoy</td>
<td>Alcoy</td>
<td>Womens</td>
<td>.39659</td>
</tr>
<tr>
<td><b>648</b></td>
<td>711</td>
<td>Sirens</td>
<td>Rideau Valley</td>
<td>Womens</td>
<td>.39654</td>
</tr>
<tr>
<td><b>649</b></td>
<td>712</td>
<td>French Broads</td>
<td>Blue Ridge</td>
<td>Womens</td>
<td>.39628</td>
</tr>
<tr>
<td><b>650</b></td>
<td>713</td>
<td>Bath City Roller Girls</td>
<td>Bath City</td>
<td>Womens</td>
<td>.39616</td>
</tr>
<tr>
<td><b>651</b></td>
<td>714</td>
<td>Kindersley Roller Derby Association</td>
<td>Crude Hitters</td>
<td>Womens</td>
<td>.39596</td>
</tr>
<tr>
<td><b>652</b></td>
<td>715</td>
<td>The Flaming Noras</td>
<td>Furness Women's</td>
<td>Womens</td>
<td>.39593</td>
</tr>
<tr>
<td><b>653</b></td>
<td>716</td>
<td>Kouvola Rock n Rollers B</td>
<td>Kouvola</td>
<td>Womens</td>
<td>.39499</td>
</tr>
<tr>
<td><b>654</b></td>
<td>717</td>
<td>Rainy City Roller Dolls</td>
<td>Rainy City (WA)</td>
<td>Womens</td>
<td>.39497</td>
</tr>
<tr>
<td><b>655</b></td>
<td>718</td>
<td>Aroostook Roller Derby</td>
<td>Aroostook</td>
<td>Womens</td>
<td>.39416</td>
</tr>
<tr>
<td><b>656</b></td>
<td>719</td>
<td>Roller Derby Tournai</td>
<td>Tournai</td>
<td>Womens</td>
<td>.39404</td>
</tr>
<tr>
<td><b>657</b></td>
<td>720</td>
<td>Crimson Vipers (Roller Derby Bergamo)</td>
<td>Bergamo</td>
<td>Womens</td>
<td>.39400</td>
</tr>
<tr>
<td><b>658</b></td>
<td>721</td>
<td>Spring Blocks</td>
<td>All Blocks</td>
<td>Womens</td>
<td>.39395</td>
</tr>
<tr>
<td><b>659</b></td>
<td>722</td>
<td>Pulp Affliction</td>
<td>ORG All-Stars</td>
<td>Womens</td>
<td>.39353</td>
</tr>
<tr>
<td><b>660</b></td>
<td>723</td>
<td>Free State Roller Derby</td>
<td>Free State</td>
<td>Womens</td>
<td>.39344</td>
</tr>
<tr>
<td><b>661</b></td>
<td>724</td>
<td>Magnolia Roller Vixens</td>
<td>Magnolia Roller Vixens</td>
<td>Womens</td>
<td>.39334</td>
</tr>
<tr>
<td><b>662</b></td>
<td>725</td>
<td>Weyburn Roller Derby Association</td>
<td>Weyburn</td>
<td>Womens</td>
<td>.39312</td>
</tr>
<tr>
<td><b>663</b></td>
<td>726</td>
<td>Roller Derby Rouen</td>
<td>Rouen</td>
<td>Womens</td>
<td>.39311</td>
</tr>
<tr>
<td><b>664</b></td>
<td>727</td>
<td>Cen-Tex Roller Girls</td>
<td>Cen-Tex</td>
<td>Womens</td>
<td>.39307</td>
</tr>
<tr>
<td><b>665</b></td>
<td>728</td>
<td>Durango Roller Girls</td>
<td>Durango</td>
<td>Womens</td>
<td>.39290</td>
</tr>
<tr>
<td><b>666</b></td>
<td>729</td>
<td>Whidbey Island Roller Girls</td>
<td>Whidbey Island</td>
<td>Womens</td>
<td>.39278</td>
</tr>
<tr>
<td><b>667</b></td>
<td>730</td>
<td>Roller Derby Pibrac</td>
<td>Pibrac</td>
<td>Womens</td>
<td>.39277</td>
</tr>
<tr>
<td><b>668</b></td>
<td>731</td>
<td>Columbia Basin Roller Derby</td>
<td>Columbia Basin</td>
<td>Womens</td>
<td>.39213</td>
</tr>
<tr>
<td><b>669</b></td>
<td>732</td>
<td>Paradise Roller Girls</td>
<td>Paradise Roller Girls</td>
<td>Womens</td>
<td>.39198</td>
</tr>
<tr>
<td><b>670</b></td>
<td>733</td>
<td>Mid State Sisters of Skate</td>
<td>Mid-State</td>
<td>Womens</td>
<td>.39156</td>
</tr>
<tr>
<td><b>671</b></td>
<td>734</td>
<td>South Shore Roller Girls</td>
<td>South Shore</td>
<td>Womens</td>
<td>.39155</td>
</tr>
<tr>
<td><b>672</b></td>
<td>735</td>
<td>Killa Hurtz Roller Girls</td>
<td>Killa Hurtz</td>
<td>Womens</td>
<td>.39155</td>
</tr>
<tr>
<td><b>673</b></td>
<td>736</td>
<td>Border City Brawlers</td>
<td>Border City Brawlers</td>
<td>Womens</td>
<td>.39153</td>
</tr>
<tr>
<td><b>674</b></td>
<td>737</td>
<td>Light City Derby (Womens)</td>
<td>Light City</td>
<td>Womens</td>
<td>.39104</td>
</tr>
<tr>
<td><b>675</b></td>
<td>738</td>
<td>Dublin Roller Derby C</td>
<td>Dublin</td>
<td>Womens</td>
<td>.39099</td>
</tr>
<tr>
<td><b>676</b></td>
<td>739</td>
<td>Block Party</td>
<td>Philly</td>
<td>Womens</td>
<td>.39018</td>
</tr>
<tr>
<td><b>677</b></td>
<td>740</td>
<td>Rockford Rage Roller Derby</td>
<td>Rockford</td>
<td>Womens</td>
<td>.38993</td>
</tr>
<tr>
<td><b>678</b></td>
<td>741</td>
<td>MedCity Mafia Roller Derby</td>
<td>Med City</td>
<td>Womens</td>
<td>.38987</td>
</tr>
<tr>
<td><b>679</b></td>
<td>742</td>
<td>Traverse City Roller Derby</td>
<td>Traverse City</td>
<td>Womens</td>
<td>.38953</td>
</tr>
<tr>
<td><b>680</b></td>
<td>743</td>
<td>Spartanburg Deadly Dolls</td>
<td>Deadly Dolls</td>
<td>Womens</td>
<td>.38914</td>
</tr>
<tr>
<td><b>681</b></td>
<td>744</td>
<td>Yellow Rose Derby Girls</td>
<td>Yellow Rose</td>
<td>Womens</td>
<td>.38830</td>
</tr>
<tr>
<td><b>682</b></td>
<td>745</td>
<td>Marietta</td>
<td>Peach State</td>
<td>Womens</td>
<td>.38808</td>
</tr>
<tr>
<td><b>683</b></td>
<td>746</td>
<td>Lethbridge Roller Derby Guild</td>
<td>Lethbridge</td>
<td>Womens</td>
<td>.38786</td>
</tr>
<tr>
<td><b>684</b></td>
<td>747</td>
<td>Surrey Roller Girls</td>
<td>Surrey (Women's)</td>
<td>Womens</td>
<td>.38775</td>
</tr>
<tr>
<td><b>685</b></td>
<td>748</td>
<td>Brawlers</td>
<td>Brandywine</td>
<td>Womens</td>
<td>.38760</td>
</tr>
<tr>
<td><b>686</b></td>
<td>749</td>
<td>Cenla Derby Dames</td>
<td>Cenla</td>
<td>Womens</td>
<td>.38674</td>
</tr>
<tr>
<td><b>687</b></td>
<td>750</td>
<td>G-Rap Attack!</td>
<td>Grand Raggidy</td>
<td>Womens</td>
<td>.38660</td>
</tr>
<tr>
<td><b>688</b></td>
<td>751</td>
<td>Kingston Derby Girls</td>
<td>Kingston</td>
<td>Womens</td>
<td>.38643</td>
</tr>
<tr>
<td><b>689</b></td>
<td>752</td>
<td>Flathead Valley Roller Derby</td>
<td>Flathead Valley</td>
<td>Womens</td>
<td>.38619</td>
</tr>
<tr>
<td><b>690</b></td>
<td>753</td>
<td>Wollongong Illawarra Roller Derby</td>
<td>Steel City Derby Dolls</td>
<td>Womens</td>
<td>.38615</td>
</tr>
<tr>
<td><b>691</b></td>
<td>754</td>
<td>Bruisin' Betties</td>
<td>Lowcountry</td>
<td>Womens</td>
<td>.38607</td>
</tr>
<tr>
<td><b>692</b></td>
<td>755</td>
<td>Wolverhampton Honour Rollers</td>
<td>Wolverhampton</td>
<td>Womens</td>
<td>.38599</td>
</tr>
<tr>
<td><b>693</b></td>
<td>756</td>
<td>Spitfires</td>
<td>Capital City</td>
<td>Womens</td>
<td>.38535</td>
</tr>
<tr>
<td><b>694</b></td>
<td>757</td>
<td>Cork City Firebirds</td>
<td>Cork City</td>
<td>Womens</td>
<td>.38524</td>
</tr>
<tr>
<td><b>695</b></td>
<td>758</td>
<td>Okanagan Derby Dolls</td>
<td>Okanagan Dolls</td>
<td>Womens</td>
<td>.38488</td>
</tr>
<tr>
<td><b>696</b></td>
<td>759</td>
<td>Perpignan Roller Derby</td>
<td>Perpignan</td>
<td>Womens</td>
<td>.38461</td>
</tr>
<tr>
<td><b>697</b></td>
<td>760</td>
<td>B Railers</td>
<td>Chattanooga</td>
<td>Womens</td>
<td>.38442</td>
</tr>
<tr>
<td><b>698</b></td>
<td>761</td>
<td>Rhein-Neckar Delta Quads</td>
<td>Delta Quads</td>
<td>Womens</td>
<td>.38439</td>
</tr>
<tr>
<td><b>699</b></td>
<td>762</td>
<td>Pensacola Roller Gurlz</td>
<td>Pensacola</td>
<td>Womens</td>
<td>.38436</td>
</tr>
<tr>
<td><b>700</b></td>
<td>763</td>
<td>Hel'z Belles Roller Derby</td>
<td>Hel'z Belles</td>
<td>Womens</td>
<td>.38406</td>
</tr>
<tr>
<td><b>701</b></td>
<td>764</td>
<td>Derby Roller Provence Méditerranée</td>
<td>Provence Méditerranée</td>
<td>Womens</td>
<td>.38403</td>
</tr>
<tr>
<td><b>702</b></td>
<td>765</td>
<td>Girls Rollin in the South</td>
<td>GRITS</td>
<td>Womens</td>
<td>.38367</td>
</tr>
<tr>
<td><b>703</b></td>
<td>766</td>
<td>SWAT B Team</td>
<td>Angels of Terror</td>
<td>Womens</td>
<td>.38365</td>
</tr>
<tr>
<td><b>704</b></td>
<td>767</td>
<td>Prince Albert Roller Derby</td>
<td>Outlaws</td>
<td>Womens</td>
<td>.38323</td>
</tr>
<tr>
<td><b>705</b></td>
<td>768</td>
<td>Aurora 88s Roller Derby</td>
<td>Aurora 88s</td>
<td>Womens</td>
<td>.38304</td>
</tr>
<tr>
<td><b>706</b></td>
<td>769</td>
<td>Roller Derby Pays d'Aix (Womens)</td>
<td>Pays d'Aix Womens</td>
<td>Womens</td>
<td>.38262</td>
</tr>
<tr>
<td><b>707</b></td>
<td>770</td>
<td>Nuclear Free Roller Derby League</td>
<td>Nuclear Free</td>
<td>Womens</td>
<td>.38219</td>
</tr>
<tr>
<td><b>708</b></td>
<td>771</td>
<td>Battery Brigade</td>
<td>Assault City</td>
<td>Womens</td>
<td>.38199</td>
</tr>
<tr>
<td><b>709</b></td>
<td>772</td>
<td>Twin City Knockers</td>
<td>Knockers</td>
<td>Womens</td>
<td>.38189</td>
</tr>
<tr>
<td><b>710</b></td>
<td>773</td>
<td>Floral City Roller Girls</td>
<td>Floral City</td>
<td>Womens</td>
<td>.38179</td>
</tr>
<tr>
<td><b>711</b></td>
<td>774</td>
<td>Mansfield Roller Derby B team</td>
<td>Mansfield</td>
<td>Womens</td>
<td>.38141</td>
</tr>
<tr>
<td><b>712</b></td>
<td>775</td>
<td>Les Bûches</td>
<td>Bûches</td>
<td>Womens</td>
<td>.38127</td>
</tr>
<tr>
<td><b>713</b></td>
<td>776</td>
<td>Joensuu Roller Derby</td>
<td>Joensuu</td>
<td>Womens</td>
<td>.38127</td>
</tr>
<tr>
<td><b>714</b></td>
<td>777</td>
<td>Forx Roller Derby</td>
<td>Forx Roller Derby</td>
<td>Womens</td>
<td>.38082</td>
</tr>
<tr>
<td><b>715</b></td>
<td>778</td>
<td>Lincolnshire Bombers</td>
<td>Lincolnshire</td>
<td>Womens</td>
<td>.38075</td>
</tr>
<tr>
<td><b>716</b></td>
<td>779</td>
<td>Durham Roller Derby</td>
<td>Durham</td>
<td>Womens</td>
<td>.38036</td>
</tr>
<tr>
<td><b>717</b></td>
<td>780</td>
<td>Piedmont Riot Roller Derby</td>
<td>Piedmont Riot</td>
<td>Womens</td>
<td>.37993</td>
</tr>
<tr>
<td><b>718</b></td>
<td>781</td>
<td>Fredericksburg Roller Derby</td>
<td>Fredericksburg</td>
<td>Womens</td>
<td>.37990</td>
</tr>
<tr>
<td><b>719</b></td>
<td>782</td>
<td>B-Sides</td>
<td>Roc City</td>
<td>Womens</td>
<td>.37963</td>
</tr>
<tr>
<td><b>720</b></td>
<td>783</td>
<td>South Florida Roller Girls</td>
<td>South Florida</td>
<td>Womens</td>
<td>.37920</td>
</tr>
<tr>
<td><b>721</b></td>
<td>784</td>
<td>The Militia</td>
<td>Dub City</td>
<td>Womens</td>
<td>.37909</td>
</tr>
<tr>
<td><b>722</b></td>
<td>785</td>
<td>Vendetta Vixens</td>
<td>Vendetta</td>
<td>Womens</td>
<td>.37889</td>
</tr>
<tr>
<td><b>723</b></td>
<td>786</td>
<td>Bad News Bs</td>
<td>Classic City</td>
<td>Womens</td>
<td>.37877</td>
</tr>
<tr>
<td><b>724</b></td>
<td>787</td>
<td>Central Maine Derby</td>
<td>Central Maine</td>
<td>Womens</td>
<td>.37841</td>
</tr>
<tr>
<td><b>725</b></td>
<td>788</td>
<td>Bath Roller Derby Girls</td>
<td>Bath Spartans</td>
<td>Womens</td>
<td>.37823</td>
</tr>
<tr>
<td><b>726</b></td>
<td>789</td>
<td>Susquehanna Valley Derby Vixens</td>
<td>Susquehanna Valley</td>
<td>Womens</td>
<td>.37807</td>
</tr>
<tr>
<td><b>727</b></td>
<td>790</td>
<td>Walla Walla Sweets Roller Girls</td>
<td>Walla Walla</td>
<td>Womens</td>
<td>.37803</td>
</tr>
<tr>
<td><b>728</b></td>
<td>791</td>
<td>Badlands Hellraisers Roller Derby</td>
<td>Hellraisers</td>
<td>Womens</td>
<td>.37762</td>
</tr>
<tr>
<td><b>729</b></td>
<td>792</td>
<td>Killa' Bees</td>
<td>Saskatoon</td>
<td>Womens</td>
<td>.37692</td>
</tr>
<tr>
<td><b>730</b></td>
<td>793</td>
<td>Battle Creek Cereal Killers</td>
<td>Battle Creek</td>
<td>Womens</td>
<td>.37690</td>
</tr>
<tr>
<td><b>731</b></td>
<td>794</td>
<td>Highland Derby Dolls</td>
<td>Highland Derby</td>
<td>Womens</td>
<td>.37679</td>
</tr>
<tr>
<td><b>732</b></td>
<td>795</td>
<td>Grin 'N' Barum Derby Girls</td>
<td>Grin 'N' Barum</td>
<td>Womens</td>
<td>.37671</td>
</tr>
<tr>
<td><b>733</b></td>
<td>796</td>
<td>Apple City Roller Derby</td>
<td>Apple City</td>
<td>Womens</td>
<td>.37643</td>
</tr>
<tr>
<td><b>734</b></td>
<td>797</td>
<td>Athens Ohio Roller Derby</td>
<td>Hell Betties</td>
<td>Womens</td>
<td>.37630</td>
</tr>
<tr>
<td><b>735</b></td>
<td>798</td>
<td>South Side Derby Dames</td>
<td>South Side (CO)</td>
<td>Womens</td>
<td>.37611</td>
</tr>
<tr>
<td><b>736</b></td>
<td>799</td>
<td>Electric City Roller GrrrlZ</td>
<td>Electric City</td>
<td>Womens</td>
<td>.37570</td>
</tr>
<tr>
<td><b>737</b></td>
<td>800</td>
<td>Platte Valley Roller Vixens</td>
<td>Platte Valley</td>
<td>Womens</td>
<td>.37556</td>
</tr>
<tr>
<td><b>738</b></td>
<td>801</td>
<td>Central Kansas Roller Girls</td>
<td>Central Kansas</td>
<td>Womens</td>
<td>.37480</td>
</tr>
<tr>
<td><b>739</b></td>
<td>802</td>
<td>Broadside Brawlers</td>
<td>Pirate City</td>
<td>Womens</td>
<td>.37462</td>
</tr>
<tr>
<td><b>740</b></td>
<td>803</td>
<td>Yankee Brutals</td>
<td>Connecticut</td>
<td>Womens</td>
<td>.37451</td>
</tr>
<tr>
<td><b>741</b></td>
<td>804</td>
<td>Red River Roller Derby</td>
<td>Red River</td>
<td>Womens</td>
<td>.37427</td>
</tr>
<tr>
<td><b>742</b></td>
<td>805</td>
<td>Code Blue Assassins</td>
<td>Bleeding Heartland</td>
<td>Womens</td>
<td>.37399</td>
</tr>
<tr>
<td><b>743</b></td>
<td>806</td>
<td>Dragon City Derby Dolls</td>
<td>Chikos</td>
<td>Womens</td>
<td>.37379</td>
</tr>
<tr>
<td><b>744</b></td>
<td>807</td>
<td>Hwy 14 Derby Association</td>
<td>Hwy 14</td>
<td>Womens</td>
<td>.37318</td>
</tr>
<tr>
<td><b>745</b></td>
<td>808</td>
<td>Quabbin Missile Crisis</td>
<td>Western Mass Destruction</td>
<td>Womens</td>
<td>.37317</td>
</tr>
<tr>
<td><b>746</b></td>
<td>809</td>
<td>Lyon Roller Derby (Womens)</td>
<td>Lyon</td>
<td>Womens</td>
<td>.37317</td>
</tr>
<tr>
<td><b>747</b></td>
<td>810</td>
<td>Wilkes-Barre/Scranton Roller Radicals</td>
<td>Roller Radicals</td>
<td>Womens</td>
<td>.37311</td>
</tr>
<tr>
<td><b>748</b></td>
<td>811</td>
<td>North Cheshire Victory Rollers</td>
<td>North Cheshire</td>
<td>Womens</td>
<td>.37292</td>
</tr>
<tr>
<td><b>749</b></td>
<td>812</td>
<td>Rogue Scholars</td>
<td>Varsity</td>
<td>Womens</td>
<td>.37279</td>
</tr>
<tr>
<td><b>750</b></td>
<td>813</td>
<td>Central West Roller Derby</td>
<td>CWA</td>
<td>Womens</td>
<td>.37267</td>
</tr>
<tr>
<td><b>751</b></td>
<td>814</td>
<td>Roller Derby Nîmes</td>
<td>Nîmes</td>
<td>Womens</td>
<td>.37252</td>
</tr>
<tr>
<td><b>752</b></td>
<td>815</td>
<td>Crime City C team</td>
<td>Crime City</td>
<td>Womens</td>
<td>.37251</td>
</tr>
<tr>
<td><b>753</b></td>
<td>816</td>
<td>Rumble Bees</td>
<td>Perth</td>
<td>Womens</td>
<td>.37240</td>
</tr>
<tr>
<td><b>754</b></td>
<td>817</td>
<td>Mean City Roller Derby (Women's)</td>
<td>Mean City Women</td>
<td>Womens</td>
<td>.37200</td>
</tr>
<tr>
<td><b>755</b></td>
<td>818</td>
<td>Cedar Rapids Rollergirls</td>
<td>Cedar Rapids Rollergirls</td>
<td>Womens</td>
<td>.37169</td>
</tr>
<tr>
<td><b>756</b></td>
<td>819</td>
<td>WestSide Derby Dollz (Women's)</td>
<td>WestSide (Women's)</td>
<td>Womens</td>
<td>.37146</td>
</tr>
<tr>
<td><b>757</b></td>
<td>820</td>
<td>Ocala Cannibals Roller Derby</td>
<td>Cannibals</td>
<td>Womens</td>
<td>.37138</td>
</tr>
<tr>
<td><b>758</b></td>
<td>821</td>
<td>Rock Villains</td>
<td>Free State</td>
<td>Womens</td>
<td>.37113</td>
</tr>
<tr>
<td><b>759</b></td>
<td>822</td>
<td>Boone Shiners</td>
<td>Appalachian Rollergirls</td>
<td>Womens</td>
<td>.37105</td>
</tr>
<tr>
<td><b>760</b></td>
<td>823</td>
<td>Morgantown Roller Vixens</td>
<td>Morgantown</td>
<td>Womens</td>
<td>.37087</td>
</tr>
<tr>
<td><b>761</b></td>
<td>824</td>
<td>Lafayette Brawlin' Dolls</td>
<td>Brawlin Dolls</td>
<td>Womens</td>
<td>.37009</td>
</tr>
<tr>
<td><b>762</b></td>
<td>825</td>
<td>Sans Culottes</td>
<td>Paris</td>
<td>Womens</td>
<td>.36972</td>
</tr>
<tr>
<td><b>763</b></td>
<td>826</td>
<td>Smoky Mountain Roller Girls</td>
<td>Smoky Mountain</td>
<td>Womens</td>
<td>.36970</td>
</tr>
<tr>
<td><b>764</b></td>
<td>827</td>
<td>Brighton Rockerbillies</td>
<td>Brighton (UK)</td>
<td>Womens</td>
<td>.36947</td>
</tr>
<tr>
<td><b>765</b></td>
<td>828</td>
<td>Monadnock Roller Derby</td>
<td>Monadnock</td>
<td>Womens</td>
<td>.36917</td>
</tr>
<tr>
<td><b>766</b></td>
<td>829</td>
<td>Chippewa Valley Roller Girls</td>
<td>Chippewa Valley</td>
<td>Womens</td>
<td>.36829</td>
</tr>
<tr>
<td><b>767</b></td>
<td>830</td>
<td>The Regulators</td>
<td>Gas City</td>
<td>Womens</td>
<td>.36816</td>
</tr>
<tr>
<td><b>768</b></td>
<td>831</td>
<td>Mouse River Rollers</td>
<td>Nodak Knockouts</td>
<td>Womens</td>
<td>.36808</td>
</tr>
<tr>
<td><b>769</b></td>
<td>832</td>
<td>Gladstone Roller Derby</td>
<td>Gladstone</td>
<td>Womens</td>
<td>.36772</td>
</tr>
<tr>
<td><b>770</b></td>
<td>833</td>
<td>Fairbanks Rollergirls</td>
<td>Fairbanks</td>
<td>Womens</td>
<td>.36645</td>
</tr>
<tr>
<td><b>771</b></td>
<td>834</td>
<td>Santas</td>
<td>Crossroads City</td>
<td>Womens</td>
<td>.36623</td>
</tr>
<tr>
<td><b>772</b></td>
<td>835</td>
<td>Åbo B-ajs</td>
<td>Dirty River</td>
<td>Womens</td>
<td>.36612</td>
</tr>
<tr>
<td><b>773</b></td>
<td>836</td>
<td>ZomB's</td>
<td>North Wales</td>
<td>Womens</td>
<td>.36591</td>
</tr>
<tr>
<td><b>774</b></td>
<td>837</td>
<td>Dread Pirate Rollers</td>
<td>Dread Pirate Rollers</td>
<td>Womens</td>
<td>.36591</td>
</tr>
<tr>
<td><b>775</b></td>
<td>838</td>
<td>Orléans Roller Derby</td>
<td>Orléans</td>
<td>Womens</td>
<td>.36575</td>
</tr>
<tr>
<td><b>776</b></td>
<td>839</td>
<td>NOVA Roller Derby</td>
<td>NOVA</td>
<td>Womens</td>
<td>.36569</td>
</tr>
<tr>
<td><b>777</b></td>
<td>840</td>
<td>Lahti Roller Derby</td>
<td>Lahti</td>
<td>Womens</td>
<td>.36511</td>
</tr>
<tr>
<td><b>778</b></td>
<td>841</td>
<td>Block Busters</td>
<td>Derby Club le Cres Lattes</td>
<td>Womens</td>
<td>.36496</td>
</tr>
<tr>
<td><b>779</b></td>
<td>842</td>
<td>York City Derby Dames</td>
<td>York City</td>
<td>Womens</td>
<td>.36480</td>
</tr>
<tr>
<td><b>780</b></td>
<td>843</td>
<td>Wakey Wheeled Cats</td>
<td>Wakefield</td>
<td>Womens</td>
<td>.36439</td>
</tr>
<tr>
<td><b>781</b></td>
<td>844</td>
<td>Beat Down</td>
<td>Jersey Shore</td>
<td>Womens</td>
<td>.36422</td>
</tr>
<tr>
<td><b>782</b></td>
<td>845</td>
<td>The Empire</td>
<td>South Side (NSW)</td>
<td>Womens</td>
<td>.36412</td>
</tr>
<tr>
<td><b>783</b></td>
<td>846</td>
<td>Carolina Bootleggers</td>
<td>Carolina</td>
<td>Womens</td>
<td>.36410</td>
</tr>
<tr>
<td><b>784</b></td>
<td>847</td>
<td>Boardwalk Brawlers</td>
<td>Shore Points</td>
<td>Womens</td>
<td>.36378</td>
</tr>
<tr>
<td><b>785</b></td>
<td>848</td>
<td>Slaughterhouse Derby Girls</td>
<td>Slaughterhouse</td>
<td>Womens</td>
<td>.36377</td>
</tr>
<tr>
<td><b>786</b></td>
<td>849</td>
<td>Roller Derby Leicester</td>
<td>Leicester</td>
<td>Womens</td>
<td>.36371</td>
</tr>
<tr>
<td><b>787</b></td>
<td>850</td>
<td>Onslaught</td>
<td>DuPage Derby</td>
<td>Womens</td>
<td>.36363</td>
</tr>
<tr>
<td><b>788</b></td>
<td>851</td>
<td>Vette City Roller Derby</td>
<td>Vette City</td>
<td>Womens</td>
<td>.36292</td>
</tr>
<tr>
<td><b>789</b></td>
<td>852</td>
<td>Rocky View Roller Derby Association</td>
<td>Rocky View</td>
<td>Womens</td>
<td>.36256</td>
</tr>
<tr>
<td><b>790</b></td>
<td>853</td>
<td>Niagara Roller Girls</td>
<td>Niagara</td>
<td>Womens</td>
<td>.36254</td>
</tr>
<tr>
<td><b>791</b></td>
<td>854</td>
<td>Middle Georgia Derby Demons</td>
<td>Middle Georgia</td>
<td>Womens</td>
<td>.36249</td>
</tr>
<tr>
<td><b>792</b></td>
<td>855</td>
<td>OKC Outlaws Roller Derby</td>
<td>OKC Outlaws</td>
<td>Womens</td>
<td>.36192</td>
</tr>
<tr>
<td><b>793</b></td>
<td>856</td>
<td>Roller Derby Creil</td>
<td>Creil</td>
<td>Womens</td>
<td>.36162</td>
</tr>
<tr>
<td><b>794</b></td>
<td>857</td>
<td>Boomtown Rollers</td>
<td>Boomtown</td>
<td>Womens</td>
<td>.36159</td>
</tr>
<tr>
<td><b>795</b></td>
<td>858</td>
<td>Orange Crush</td>
<td>Dutchland</td>
<td>Womens</td>
<td>.36131</td>
</tr>
<tr>
<td><b>796</b></td>
<td>859</td>
<td>Molly's Marauders</td>
<td>Molly Roger</td>
<td>Womens</td>
<td>.36127</td>
</tr>
<tr>
<td><b>797</b></td>
<td>860</td>
<td>Bloody Bordens</td>
<td>Mass Attack</td>
<td>Womens</td>
<td>.36102</td>
</tr>
<tr>
<td><b>798</b></td>
<td>861</td>
<td>Roller Derby Tarbes</td>
<td>Tarbes</td>
<td>Womens</td>
<td>.36099</td>
</tr>
<tr>
<td><b>799</b></td>
<td>862</td>
<td>Waimea Wranglers</td>
<td>Waimea</td>
<td>Womens</td>
<td>.36089</td>
</tr>
<tr>
<td><b>800</b></td>
<td>863</td>
<td>Alp'n Rockets Roller Derby</td>
<td>Alp'n Rockets</td>
<td>Womens</td>
<td>.36064</td>
</tr>
<tr>
<td><b>801</b></td>
<td>864</td>
<td>Inner West Roller Derby League</td>
<td>Inner West</td>
<td>Womens</td>
<td>.36030</td>
</tr>
<tr>
<td><b>802</b></td>
<td>865</td>
<td>Diamond Roughcuts</td>
<td>Diamond Divas</td>
<td>Womens</td>
<td>.36023</td>
</tr>
<tr>
<td><b>803</b></td>
<td>866</td>
<td>Harbor City Roller Dames</td>
<td>Harbor City</td>
<td>Womens</td>
<td>.36022</td>
</tr>
<tr>
<td><b>804</b></td>
<td>867</td>
<td>BisMan Bombzillaz</td>
<td>Bombshellz</td>
<td>Womens</td>
<td>.36011</td>
</tr>
<tr>
<td><b>805</b></td>
<td>868</td>
<td>Violet Femmes</td>
<td>Gem City</td>
<td>Womens</td>
<td>.36007</td>
</tr>
<tr>
<td><b>806</b></td>
<td>869</td>
<td>Rotten Cherries</td>
<td>Black Rose Rollers</td>
<td>Womens</td>
<td>.35975</td>
</tr>
<tr>
<td><b>807</b></td>
<td>870</td>
<td>Assault City Roller Derby</td>
<td>Assault City</td>
<td>Womens</td>
<td>.35955</td>
</tr>
<tr>
<td><b>808</b></td>
<td>871</td>
<td>Glass City B Team</td>
<td>Glass City</td>
<td>Womens</td>
<td>.35928</td>
</tr>
<tr>
<td><b>809</b></td>
<td>872</td>
<td>North Wales Roller Derby</td>
<td>North Wales</td>
<td>Womens</td>
<td>.35872</td>
</tr>
<tr>
<td><b>810</b></td>
<td>873</td>
<td>Key West Derby Dames</td>
<td>Key West</td>
<td>Womens</td>
<td>.35857</td>
</tr>
<tr>
<td><b>811</b></td>
<td>874</td>
<td>Capital Defenders</td>
<td>Red Stick</td>
<td>Womens</td>
<td>.35851</td>
</tr>
<tr>
<td><b>812</b></td>
<td>875</td>
<td>Emerald Coast Roller Derby</td>
<td>Emerald Coast</td>
<td>Womens</td>
<td>.35838</td>
</tr>
<tr>
<td><b>813</b></td>
<td>876</td>
<td>River City Dames Of Anarchy</td>
<td>Dames of Anarchy</td>
<td>Womens</td>
<td>.35834</td>
</tr>
<tr>
<td><b>814</b></td>
<td>877</td>
<td>Zaragoza Roller Derby</td>
<td>Zaragoza</td>
<td>Womens</td>
<td>.35810</td>
</tr>
<tr>
<td><b>815</b></td>
<td>878</td>
<td>Namur Roller Girls B</td>
<td>Namur</td>
<td>Womens</td>
<td>.35782</td>
</tr>
<tr>
<td><b>816</b></td>
<td>879</td>
<td>Nickel City Roller Derby</td>
<td>Nickel City</td>
<td>Womens</td>
<td>.35780</td>
</tr>
<tr>
<td><b>817</b></td>
<td>880</td>
<td>Killa Crew</td>
<td>Killamazoo</td>
<td>Womens</td>
<td>.35740</td>
</tr>
<tr>
<td><b>818</b></td>
<td>881</td>
<td>Armidale Roller Derby</td>
<td>Armidale</td>
<td>Womens</td>
<td>.35693</td>
</tr>
<tr>
<td><b>819</b></td>
<td>882</td>
<td>Conroe Roller Derby</td>
<td>Conroe Cutthroats</td>
<td>Womens</td>
<td>.35652</td>
</tr>
<tr>
<td><b>820</b></td>
<td>883</td>
<td>South Coast Roller Girls</td>
<td>South Coast</td>
<td>Womens</td>
<td>.35632</td>
</tr>
<tr>
<td><b>821</b></td>
<td>884</td>
<td>Motown Wreckers</td>
<td>Detroit</td>
<td>Womens</td>
<td>.35603</td>
</tr>
<tr>
<td><b>822</b></td>
<td>885</td>
<td>Greenbrier River Rollers</td>
<td>Greenbrier</td>
<td>Womens</td>
<td>.35588</td>
</tr>
<tr>
<td><b>823</b></td>
<td>886</td>
<td>B.ADD</td>
<td>Amsterdam</td>
<td>Womens</td>
<td>.35585</td>
</tr>
<tr>
<td><b>824</b></td>
<td>887</td>
<td>AAA</td>
<td>Omaha</td>
<td>Womens</td>
<td>.35565</td>
</tr>
<tr>
<td><b>825</b></td>
<td>888</td>
<td>Haunted City Rollers</td>
<td>Haunted City</td>
<td>Womens</td>
<td>.35538</td>
</tr>
<tr>
<td><b>826</b></td>
<td>889</td>
<td>Beach Brawl SK8R Dolls</td>
<td>Beach Brawl</td>
<td>Womens</td>
<td>.35528</td>
</tr>
<tr>
<td><b>827</b></td>
<td>890</td>
<td>Seacoast Roller Derby</td>
<td>Poison Pixies</td>
<td>Womens</td>
<td>.35527</td>
</tr>
<tr>
<td><b>828</b></td>
<td>891</td>
<td>BADD Intentions</td>
<td>Beckley</td>
<td>Womens</td>
<td>.35454</td>
</tr>
<tr>
<td><b>829</b></td>
<td>892</td>
<td>J-Villains</td>
<td>Jacksonville</td>
<td>Womens</td>
<td>.35448</td>
</tr>
<tr>
<td><b>830</b></td>
<td>893</td>
<td>Rollerderby Hannover</td>
<td>Hannover</td>
<td>Womens</td>
<td>.35433</td>
</tr>
<tr>
<td><b>831</b></td>
<td>894</td>
<td>Porto Beasts</td>
<td>Porto</td>
<td>Womens</td>
<td>.35425</td>
</tr>
<tr>
<td><b>832</b></td>
<td>895</td>
<td>Nasty Nancies</td>
<td>Brisbane City</td>
<td>Womens</td>
<td>.35419</td>
</tr>
<tr>
<td><b>833</b></td>
<td>896</td>
<td>Biodegradables</td>
<td>Recycled Rollers</td>
<td>Womens</td>
<td>.35319</td>
</tr>
<tr>
<td><b>834</b></td>
<td>897</td>
<td>Swamp City Sirens</td>
<td>Gainesville</td>
<td>Womens</td>
<td>.35300</td>
</tr>
<tr>
<td><b>835</b></td>
<td>898</td>
<td>B.M.O. Roller Derby Girls</td>
<td>Brest</td>
<td>Womens</td>
<td>.35258</td>
</tr>
<tr>
<td><b>836</b></td>
<td>899</td>
<td>Aalborg Roller Derby</td>
<td>Aalborg</td>
<td>Womens</td>
<td>.35252</td>
</tr>
<tr>
<td><b>837</b></td>
<td>900</td>
<td>Beastie Derby Girls</td>
<td>Reims</td>
<td>Womens</td>
<td>.35251</td>
</tr>
<tr>
<td><b>838</b></td>
<td>901</td>
<td>St. Cloud Area Roller Dolls</td>
<td>SCAR Dolls</td>
<td>Womens</td>
<td>.35249</td>
</tr>
<tr>
<td><b>839</b></td>
<td>902</td>
<td>Devil State Derby League</td>
<td>Devil State</td>
<td>Womens</td>
<td>.35175</td>
</tr>
<tr>
<td><b>840</b></td>
<td>903</td>
<td>Brute Squad</td>
<td>Brandywine</td>
<td>Womens</td>
<td>.35156</td>
</tr>
<tr>
<td><b>841</b></td>
<td>904</td>
<td>Bomb Squad</td>
<td>Blitz Dames</td>
<td>Womens</td>
<td>.35066</td>
</tr>
<tr>
<td><b>842</b></td>
<td>905</td>
<td>Natural Disasters</td>
<td>NW Arkansas</td>
<td>Womens</td>
<td>.35022</td>
</tr>
<tr>
<td><b>843</b></td>
<td>906</td>
<td>Croydon Vice Squad</td>
<td>Croydon</td>
<td>Womens</td>
<td>.35022</td>
</tr>
<tr>
<td><b>844</b></td>
<td>907</td>
<td>Panthers Miaou</td>
<td>Panthers Graou</td>
<td>Womens</td>
<td>.34986</td>
</tr>
<tr>
<td><b>845</b></td>
<td>908</td>
<td>Rum City Derby Dolls</td>
<td>Rum City</td>
<td>Womens</td>
<td>.34955</td>
</tr>
<tr>
<td><b>846</b></td>
<td>909</td>
<td>Black Shucks</td>
<td>Norfolk</td>
<td>Womens</td>
<td>.34907</td>
</tr>
<tr>
<td><b>847</b></td>
<td>910</td>
<td>Babe City Rollers</td>
<td>Babe City</td>
<td>Womens</td>
<td>.34904</td>
</tr>
<tr>
<td><b>848</b></td>
<td>911</td>
<td>Gin City Rollers</td>
<td>Plymouth</td>
<td>Womens</td>
<td>.34891</td>
</tr>
<tr>
<td><b>849</b></td>
<td>912</td>
<td>Harbor Girls B</td>
<td>St. Pauli</td>
<td>Womens</td>
<td>.34853</td>
</tr>
<tr>
<td><b>850</b></td>
<td>913</td>
<td>Riot Rollers Darmstadt</td>
<td>Darmstadt</td>
<td>Womens</td>
<td>.34755</td>
</tr>
<tr>
<td><b>851</b></td>
<td>914</td>
<td>Outcast Derby</td>
<td>Outcast</td>
<td>Womens</td>
<td>.34735</td>
</tr>
<tr>
<td><b>852</b></td>
<td>915</td>
<td>Spindletop Rollergirls</td>
<td>Spindletop</td>
<td>Womens</td>
<td>.34707</td>
</tr>
<tr>
<td><b>853</b></td>
<td>916</td>
<td>Castle Rock 'n' Rollers</td>
<td>Castle Rock</td>
<td>Womens</td>
<td>.34695</td>
</tr>
<tr>
<td><b>854</b></td>
<td>917</td>
<td>Acadiana Roller Girls</td>
<td>Acadiana</td>
<td>Womens</td>
<td>.34668</td>
</tr>
<tr>
<td><b>855</b></td>
<td>918</td>
<td>Eastbourne Roller Derby (Womens)</td>
<td>Eastbourne Womens</td>
<td>Womens</td>
<td>.34667</td>
</tr>
<tr>
<td><b>856</b></td>
<td>919</td>
<td>Severn Roller Torrent</td>
<td>Severn</td>
<td>Womens</td>
<td>.34633</td>
</tr>
<tr>
<td><b>857</b></td>
<td>920</td>
<td>Seven Valley Rollers</td>
<td>7 Valley</td>
<td>Womens</td>
<td>.34539</td>
</tr>
<tr>
<td><b>858</b></td>
<td>921</td>
<td>Bunbury Roller Derby</td>
<td>Bunbury</td>
<td>Womens</td>
<td>.34526</td>
</tr>
<tr>
<td><b>859</b></td>
<td>922</td>
<td>Freaky Mons'ter Derby Ladies</td>
<td>Mons</td>
<td>Womens</td>
<td>.34515</td>
</tr>
<tr>
<td><b>860</b></td>
<td>923</td>
<td>Nancy Roller Derby</td>
<td>Nancy</td>
<td>Womens</td>
<td>.34496</td>
</tr>
<tr>
<td><b>861</b></td>
<td>924</td>
<td>Bluestockings</td>
<td>Ithaca</td>
<td>Womens</td>
<td>.34494</td>
</tr>
<tr>
<td><b>862</b></td>
<td>925</td>
<td>Roller Derby Bordeaux</td>
<td>Bordeaux</td>
<td>Womens</td>
<td>.34401</td>
</tr>
<tr>
<td><b>863</b></td>
<td>926</td>
<td>Blue Mountains Roller Derby League</td>
<td>Blue Mountains</td>
<td>Womens</td>
<td>.34388</td>
</tr>
<tr>
<td><b>864</b></td>
<td>927</td>
<td>Hurricane Alley Roller Derby</td>
<td>Hurricane Alley</td>
<td>Womens</td>
<td>.34361</td>
</tr>
<tr>
<td><b>865</b></td>
<td>928</td>
<td>Roller Derby Karlsruhe</td>
<td>Karlsruhe</td>
<td>Womens</td>
<td>.34322</td>
</tr>
<tr>
<td><b>866</b></td>
<td>929</td>
<td>301 Derby Dames</td>
<td>301 Derby</td>
<td>Womens</td>
<td>.34230</td>
</tr>
<tr>
<td><b>867</b></td>
<td>930</td>
<td>Sugar Sands Roller Dolls</td>
<td>Sugar Sands</td>
<td>Womens</td>
<td>.34218</td>
</tr>
<tr>
<td><b>868</b></td>
<td>931</td>
<td>Roller Derby Dijon</td>
<td>Dijon</td>
<td>Womens</td>
<td>.34164</td>
</tr>
<tr>
<td><b>869</b></td>
<td>932</td>
<td>Denali Destroyers</td>
<td>Destroyer Dolls</td>
<td>Womens</td>
<td>.34117</td>
</tr>
<tr>
<td><b>870</b></td>
<td>933</td>
<td>Wrangell Roller Derby</td>
<td>Wrangell</td>
<td>Womens</td>
<td>.34109</td>
</tr>
<tr>
<td><b>871</b></td>
<td>934</td>
<td>Upstate Roller Girl Evolution</td>
<td>URGE</td>
<td>Womens</td>
<td>.34063</td>
</tr>
<tr>
<td><b>872</b></td>
<td>935</td>
<td>Heartland Havoc</td>
<td>ICT</td>
<td>Womens</td>
<td>.34056</td>
</tr>
<tr>
<td><b>873</b></td>
<td>936</td>
<td>Muncie MissFits</td>
<td>Cornfed</td>
<td>Womens</td>
<td>.33962</td>
</tr>
<tr>
<td><b>874</b></td>
<td>937</td>
<td>Slay Belles</td>
<td>Central City</td>
<td>Womens</td>
<td>.33961</td>
</tr>
<tr>
<td><b>875</b></td>
<td>938</td>
<td>East Lansing Roller Derby</td>
<td>East Lansing</td>
<td>Womens</td>
<td>.33959</td>
</tr>
<tr>
<td><b>876</b></td>
<td>939</td>
<td>Heart of Appalachia Roller Derby</td>
<td>Heart of Appalachia</td>
<td>Womens</td>
<td>.33941</td>
</tr>
<tr>
<td><b>877</b></td>
<td>940</td>
<td>Los Alamos Derby Dames</td>
<td>Los Alamos</td>
<td>Womens</td>
<td>.33917</td>
</tr>
<tr>
<td><b>878</b></td>
<td>941</td>
<td>St. Albert Heavenly Rollers Derby</td>
<td>Heavenly Rollers</td>
<td>Womens</td>
<td>.33912</td>
</tr>
<tr>
<td><b>879</b></td>
<td>942</td>
<td>Northern Allegheny Roller Derby</td>
<td>Northern Allegheny</td>
<td>Womens</td>
<td>.33903</td>
</tr>
<tr>
<td><b>880</b></td>
<td>943</td>
<td>Diamond City Roller Derby</td>
<td>Diamond City</td>
<td>Womens</td>
<td>.33898</td>
</tr>
<tr>
<td><b>881</b></td>
<td>944</td>
<td>South Central Roller Girls</td>
<td>South Central</td>
<td>Womens</td>
<td>.33868</td>
</tr>
<tr>
<td><b>882</b></td>
<td>945</td>
<td>Bux-Mont Roller Derby Dolls</td>
<td>Bux-Mont</td>
<td>Womens</td>
<td>.33821</td>
</tr>
<tr>
<td><b>883</b></td>
<td>946</td>
<td>Downriver Muscle</td>
<td>Downriver</td>
<td>Womens</td>
<td>.33741</td>
</tr>
<tr>
<td><b>884</b></td>
<td>947</td>
<td>Garden Island Renegade Rollerz</td>
<td>G.I. Renegade Rollerz</td>
<td>Womens</td>
<td>.33706</td>
</tr>
<tr>
<td><b>885</b></td>
<td>948</td>
<td>The Jokers</td>
<td>The Parliament of Pain</td>
<td>Womens</td>
<td>.33698</td>
</tr>
<tr>
<td><b>886</b></td>
<td>949</td>
<td>Sarnia Roller Derby League</td>
<td>Sarnia</td>
<td>Womens</td>
<td>.33697</td>
</tr>
<tr>
<td><b>887</b></td>
<td>950</td>
<td>Rotterdam Killer Bees</td>
<td>Rotterdam</td>
<td>Womens</td>
<td>.33694</td>
</tr>
<tr>
<td><b>888</b></td>
<td>951</td>
<td>Orlando Roller Derby B</td>
<td>Psycho City</td>
<td>Womens</td>
<td>.33670</td>
</tr>
<tr>
<td><b>889</b></td>
<td>952</td>
<td>Rollergirls Of Central Kentucky</td>
<td>R.O.C.K.</td>
<td>Womens</td>
<td>.33622</td>
</tr>
<tr>
<td><b>890</b></td>
<td>953</td>
<td>New River Knockouts</td>
<td>New River</td>
<td>Womens</td>
<td>.33616</td>
</tr>
<tr>
<td><b>891</b></td>
<td>954</td>
<td>Festival City Rollergirls</td>
<td>Festival City</td>
<td>Womens</td>
<td>.33532</td>
</tr>
<tr>
<td><b>892</b></td>
<td>955</td>
<td>Roller Derby Madrid B</td>
<td>Madrid</td>
<td>Womens</td>
<td>.33493</td>
</tr>
<tr>
<td><b>893</b></td>
<td>956</td>
<td>Capital City Roller Girls</td>
<td>Capital City</td>
<td>Womens</td>
<td>.33470</td>
</tr>
<tr>
<td><b>894</b></td>
<td>957</td>
<td>Third Alarm</td>
<td>Naptown</td>
<td>Womens</td>
<td>.33364</td>
</tr>
<tr>
<td><b>895</b></td>
<td>958</td>
<td>The York Minxters</td>
<td>York</td>
<td>Womens</td>
<td>.33352</td>
</tr>
<tr>
<td><b>896</b></td>
<td>959</td>
<td>New Generation</td>
<td>Antwerp</td>
<td>Womens</td>
<td>.33348</td>
</tr>
<tr>
<td><b>897</b></td>
<td>960</td>
<td>Reaper Roller Derby</td>
<td>Reaper</td>
<td>Womens</td>
<td>.33342</td>
</tr>
<tr>
<td><b>898</b></td>
<td>961</td>
<td>Tulsa Derby League</td>
<td>Tulsa Derby Brigade</td>
<td>Womens</td>
<td>.33333</td>
</tr>
<tr>
<td><b>899</b></td>
<td>962</td>
<td>Gillette Roller Derby</td>
<td>Miners' Daughters</td>
<td>Womens</td>
<td>.33267</td>
</tr>
<tr>
<td><b>900</b></td>
<td>963</td>
<td>Jailbreak Betties</td>
<td>Tallahassee</td>
<td>Womens</td>
<td>.33256</td>
</tr>
<tr>
<td><b>901</b></td>
<td>964</td>
<td>Keweenaw Roller Girls</td>
<td>Keweenaw</td>
<td>Womens</td>
<td>.33243</td>
</tr>
<tr>
<td><b>902</b></td>
<td>965</td>
<td>Udder Team</td>
<td>Milton Keynes</td>
<td>Womens</td>
<td>.33213</td>
</tr>
<tr>
<td><b>903</b></td>
<td>966</td>
<td>Jyväskylä Roller Derby</td>
<td>Jyväskylä</td>
<td>Womens</td>
<td>.33207</td>
</tr>
<tr>
<td><b>904</b></td>
<td>967</td>
<td>Baronnes Von Schlass</td>
<td>Switchblade</td>
<td>Womens</td>
<td>.33167</td>
</tr>
<tr>
<td><b>905</b></td>
<td>968</td>
<td>Mississippi Rollergirls</td>
<td>Mississippi Rollergirls</td>
<td>Womens</td>
<td>.33118</td>
</tr>
<tr>
<td><b>906</b></td>
<td>969</td>
<td>Convicts</td>
<td>Richter City</td>
<td>Womens</td>
<td>.33102</td>
</tr>
<tr>
<td><b>907</b></td>
<td>970</td>
<td>Southern Illinois Roller Girls</td>
<td>So Ill</td>
<td>Womens</td>
<td>.33047</td>
</tr>
<tr>
<td><b>908</b></td>
<td>971</td>
<td>Breaking Bears</td>
<td>Bear City</td>
<td>Womens</td>
<td>.32937</td>
</tr>
<tr>
<td><b>909</b></td>
<td>972</td>
<td>Sulphur City Steam Rollers</td>
<td>Sulphur City</td>
<td>Womens</td>
<td>.32916</td>
</tr>
<tr>
<td><b>910</b></td>
<td>973</td>
<td>Confluence Crush Roller Derby</td>
<td>Confluence</td>
<td>Womens</td>
<td>.32910</td>
</tr>
<tr>
<td><b>911</b></td>
<td>974</td>
<td>Western Sydney Rollers</td>
<td>Western Sydney</td>
<td>Womens</td>
<td>.32906</td>
</tr>
<tr>
<td><b>912</b></td>
<td>975</td>
<td>Roller Derby Rennes - équipe B</td>
<td>Rennes</td>
<td>Womens</td>
<td>.32899</td>
</tr>
<tr>
<td><b>913</b></td>
<td>976</td>
<td>Grey Bruce Roller Derby</td>
<td>Grey Bruce</td>
<td>Womens</td>
<td>.32862</td>
</tr>
<tr>
<td><b>914</b></td>
<td>977</td>
<td>C-kasetti</td>
<td>Helsinki</td>
<td>Womens</td>
<td>.32837</td>
</tr>
<tr>
<td><b>915</b></td>
<td>978</td>
<td>Stone Cold Foxes</td>
<td>Stone Cold Foxes</td>
<td>Womens</td>
<td>.32812</td>
</tr>
<tr>
<td><b>916</b></td>
<td>979</td>
<td>Dothan Roller Derby</td>
<td>Dothan</td>
<td>Womens</td>
<td>.32785</td>
</tr>
<tr>
<td><b>917</b></td>
<td>980</td>
<td>Bazooka Janes</td>
<td>Capital City</td>
<td>Womens</td>
<td>.32700</td>
</tr>
<tr>
<td><b>918</b></td>
<td>981</td>
<td>Yellow Shovemarines</td>
<td>Liverpool</td>
<td>Womens</td>
<td>.32651</td>
</tr>
<tr>
<td><b>919</b></td>
<td>982</td>
<td>Petersburg Ragnarök Rollers</td>
<td>Petersburg Ragnarök Rollers</td>
<td>Womens</td>
<td>.32637</td>
</tr>
<tr>
<td><b>920</b></td>
<td>983</td>
<td>Lisboa Roller Derby</td>
<td>Lisboa</td>
<td>Womens</td>
<td>.32632</td>
</tr>
<tr>
<td><b>921</b></td>
<td>984</td>
<td>Roller Derby Lorient</td>
<td>Lorient</td>
<td>Womens</td>
<td>.32569</td>
</tr>
<tr>
<td><b>922</b></td>
<td>985</td>
<td>Tiger Lilies</td>
<td>Wirral (Women's)</td>
<td>Womens</td>
<td>.32537</td>
</tr>
<tr>
<td><b>923</b></td>
<td>986</td>
<td>Gapland Rollers</td>
<td>Gapland</td>
<td>Womens</td>
<td>.32534</td>
</tr>
<tr>
<td><b>924</b></td>
<td>987</td>
<td>Brighton Roller Dollz</td>
<td>Brighton (MI)</td>
<td>Womens</td>
<td>.32516</td>
</tr>
<tr>
<td><b>925</b></td>
<td>988</td>
<td>Pacific Roller Derby</td>
<td>Pacific</td>
<td>Womens</td>
<td>.32491</td>
</tr>
<tr>
<td><b>926</b></td>
<td>989</td>
<td>Suck City Rock 'n Roller Dolls</td>
<td>Suck City</td>
<td>Womens</td>
<td>.32475</td>
</tr>
<tr>
<td><b>927</b></td>
<td>990</td>
<td>PLAP City Rollers</td>
<td>PLAP City</td>
<td>Womens</td>
<td>.32414</td>
</tr>
<tr>
<td><b>928</b></td>
<td>991</td>
<td>Battlefield Roller Derby</td>
<td>Battlefield</td>
<td>Womens</td>
<td>.32412</td>
</tr>
<tr>
<td><b>929</b></td>
<td>992</td>
<td>The Bet Lynch Mob</td>
<td>Rainy City (UK)</td>
<td>Womens</td>
<td>.32375</td>
</tr>
<tr>
<td><b>930</b></td>
<td>993</td>
<td>Mississippi Brawl Stars</td>
<td>Brawl Stars</td>
<td>Womens</td>
<td>.32371</td>
</tr>
<tr>
<td><b>931</b></td>
<td>994</td>
<td>Grim Reavers</td>
<td>Grim Reavers</td>
<td>Womens</td>
<td>.32335</td>
</tr>
<tr>
<td><b>932</b></td>
<td>995</td>
<td>Counterstrike</td>
<td>Greensboro</td>
<td>Womens</td>
<td>.32299</td>
</tr>
<tr>
<td><b>933</b></td>
<td>996</td>
<td>Taxider'Biches Thonon</td>
<td>Taxider'Biches</td>
<td>Womens</td>
<td>.32296</td>
</tr>
<tr>
<td><b>934</b></td>
<td>997</td>
<td>Blood, Bath, and Beyond</td>
<td>Bath City</td>
<td>Womens</td>
<td>.32288</td>
</tr>
<tr>
<td><b>935</b></td>
<td>998</td>
<td>Central Michigan Roller Derby</td>
<td>Central Michigan</td>
<td>Womens</td>
<td>.32262</td>
</tr>
<tr>
<td><b>936</b></td>
<td>999</td>
<td>Hammer City Harlots</td>
<td>Hammer City</td>
<td>Womens</td>
<td>.32255</td>
</tr>
<tr>
<td><b>937</b></td>
<td>1000</td>
<td>Riot City Ravens</td>
<td>Riot City Ravens</td>
<td>Womens</td>
<td>.32154</td>
</tr>
<tr>
<td><b>938</b></td>
<td>1001</td>
<td>Trouble Makers</td>
<td>Charm City</td>
<td>Womens</td>
<td>.32134</td>
</tr>
<tr>
<td><b>939</b></td>
<td>1002</td>
<td>Roller Derby Calaisis (Women's)</td>
<td>Calais (Women's)</td>
<td>Womens</td>
<td>.32126</td>
</tr>
<tr>
<td><b>940</b></td>
<td>1003</td>
<td>Renfrew County Roller Derby</td>
<td>Renfrew County</td>
<td>Womens</td>
<td>.32074</td>
</tr>
<tr>
<td><b>941</b></td>
<td>1004</td>
<td>Copper City Queens Roller Derby</td>
<td>Copper City</td>
<td>Womens</td>
<td>.32028</td>
</tr>
<tr>
<td><b>942</b></td>
<td>1005</td>
<td>Roller Derby Sherbrooke</td>
<td>Sherbrooke</td>
<td>Womens</td>
<td>.31994</td>
</tr>
<tr>
<td><b>943</b></td>
<td>1006</td>
<td>Roller Derby Genève</td>
<td>Leman'Wheels</td>
<td>Womens</td>
<td>.31981</td>
</tr>
<tr>
<td><b>944</b></td>
<td>1007</td>
<td>Mansfield Roller Derby</td>
<td>Mansfield</td>
<td>Womens</td>
<td>.31914</td>
</tr>
<tr>
<td><b>945</b></td>
<td>1008</td>
<td>Lightning Broads</td>
<td>Oklahoma City</td>
<td>Womens</td>
<td>.31883</td>
</tr>
<tr>
<td><b>946</b></td>
<td>1009</td>
<td>Rocktown Rollers</td>
<td>Rocktown</td>
<td>Womens</td>
<td>.31865</td>
</tr>
<tr>
<td><b>947</b></td>
<td>1010</td>
<td>Goosetown Roller Girls</td>
<td>Goosetown</td>
<td>Womens</td>
<td>.31770</td>
</tr>
<tr>
<td><b>948</b></td>
<td>1011</td>
<td>Virgin Marys</td>
<td>Geelong</td>
<td>Womens</td>
<td>.31763</td>
</tr>
<tr>
<td><b>949</b></td>
<td>1012</td>
<td>Shanghaied Roller Dolls</td>
<td>Shanghaied</td>
<td>Womens</td>
<td>.31692</td>
</tr>
<tr>
<td><b>950</b></td>
<td>1013</td>
<td>Kill Devil Derby Brigade</td>
<td>Kill Devil</td>
<td>Womens</td>
<td>.31672</td>
</tr>
<tr>
<td><b>951</b></td>
<td>1014</td>
<td>Albuquerque Roller Derby (Womens)</td>
<td>Albuquerque Roller Derby(W)</td>
<td>Womens</td>
<td>.31599</td>
</tr>
<tr>
<td><b>952</b></td>
<td>1015</td>
<td>Roll'in Tarn Roller Derby</td>
<td>Roll'in Tarn</td>
<td>Womens</td>
<td>.31559</td>
</tr>
<tr>
<td><b>953</b></td>
<td>1016</td>
<td>Arnhem Fallen Angels</td>
<td>Arnhem</td>
<td>Womens</td>
<td>.31554</td>
</tr>
<tr>
<td><b>954</b></td>
<td>1017</td>
<td>Killa Geishas of Misawa</td>
<td>Killa Geishas</td>
<td>Womens</td>
<td>.31430</td>
</tr>
<tr>
<td><b>955</b></td>
<td>1018</td>
<td>Plan B</td>
<td>Dock City</td>
<td>Womens</td>
<td>.31418</td>
</tr>
<tr>
<td><b>956</b></td>
<td>1019</td>
<td>Shee Devils</td>
<td>Sitka</td>
<td>Womens</td>
<td>.31414</td>
</tr>
<tr>
<td><b>957</b></td>
<td>1020</td>
<td>Southern Delaware Rollergirls</td>
<td>Southern Delaware</td>
<td>Womens</td>
<td>.31400</td>
</tr>
<tr>
<td><b>958</b></td>
<td>1021</td>
<td>Porvoo Roller Derby</td>
<td>Porvoo</td>
<td>Womens</td>
<td>.31355</td>
</tr>
<tr>
<td><b>959</b></td>
<td>1022</td>
<td>Paris Hockey Club</td>
<td>Les Gueuses A</td>
<td>Womens</td>
<td>.31347</td>
</tr>
<tr>
<td><b>960</b></td>
<td>1023</td>
<td>Roskilde Roller Derby</td>
<td>Roskilde</td>
<td>Womens</td>
<td>.31331</td>
</tr>
<tr>
<td><b>961</b></td>
<td>1024</td>
<td>Badda Bings</td>
<td>Swamp City</td>
<td>Womens</td>
<td>.31301</td>
</tr>
<tr>
<td><b>962</b></td>
<td>1025</td>
<td>Nidaros Killer B's</td>
<td>Nidaros</td>
<td>Womens</td>
<td>.31286</td>
</tr>
<tr>
<td><b>963</b></td>
<td>1026</td>
<td>Rust Belt Rollers</td>
<td>Little Steel Derby Girls</td>
<td>Womens</td>
<td>.31243</td>
</tr>
<tr>
<td><b>964</b></td>
<td>1027</td>
<td>Roller Derby Rimouski</td>
<td>Rimouski</td>
<td>Womens</td>
<td>.31233</td>
</tr>
<tr>
<td><b>965</b></td>
<td>1028</td>
<td>Vienna Beasts</td>
<td>Vienna</td>
<td>Womens</td>
<td>.31187</td>
</tr>
<tr>
<td><b>966</b></td>
<td>1029</td>
<td>Belleville Roller Derby</td>
<td>Belleville</td>
<td>Womens</td>
<td>.31180</td>
</tr>
<tr>
<td><b>967</b></td>
<td>1030</td>
<td>Scarlet Fever</td>
<td>Wheat City</td>
<td>Womens</td>
<td>.31148</td>
</tr>
<tr>
<td><b>968</b></td>
<td>1031</td>
<td>Sintral Florida Derby Demons</td>
<td>Sintral</td>
<td>Womens</td>
<td>.31133</td>
</tr>
<tr>
<td><b>969</b></td>
<td>1032</td>
<td>Team Griffin</td>
<td>Northern Brisbane</td>
<td>Womens</td>
<td>.31092</td>
</tr>
<tr>
<td><b>970</b></td>
<td>1033</td>
<td>Bath Roman Rollers</td>
<td>Bath Spartans</td>
<td>Womens</td>
<td>.31075</td>
</tr>
<tr>
<td><b>971</b></td>
<td>1034</td>
<td>Kuopio Roller Derby</td>
<td>Kuopio</td>
<td>Womens</td>
<td>.31036</td>
</tr>
<tr>
<td><b>972</b></td>
<td>1035</td>
<td>Rabbit Skulls Roller Derby Avignon</td>
<td>Rabbit Skulls</td>
<td>Womens</td>
<td>.30992</td>
</tr>
<tr>
<td><b>973</b></td>
<td>1036</td>
<td>Herculadies</td>
<td>Hellions</td>
<td>Womens</td>
<td>.30984</td>
</tr>
<tr>
<td><b>974</b></td>
<td>1037</td>
<td>Howlin' Rolls</td>
<td>Tampere</td>
<td>Womens</td>
<td>.30970</td>
</tr>
<tr>
<td><b>975</b></td>
<td>1038</td>
<td>South Simcoe Rebel Rollers</td>
<td>South Simcoe</td>
<td>Womens</td>
<td>.30917</td>
</tr>
<tr>
<td><b>976</b></td>
<td>1039</td>
<td>B-Dazzlers</td>
<td>Charlotte</td>
<td>Womens</td>
<td>.30910</td>
</tr>
<tr>
<td><b>977</b></td>
<td>1040</td>
<td>Terrorz of Tiny Towns</td>
<td>Diesel Dollz</td>
<td>Womens</td>
<td>.30864</td>
</tr>
<tr>
<td><b>978</b></td>
<td>1041</td>
<td>Bodø Roller Derby</td>
<td>Bodø</td>
<td>Womens</td>
<td>.30859</td>
</tr>
<tr>
<td><b>979</b></td>
<td>1042</td>
<td>Oxford Wheels of Gory Roller Derby</td>
<td>Wheels of Gory</td>
<td>Womens</td>
<td>.30838</td>
</tr>
<tr>
<td><b>980</b></td>
<td>1043</td>
<td>Second Line</td>
<td>Big Easy</td>
<td>Womens</td>
<td>.30814</td>
</tr>
<tr>
<td><b>981</b></td>
<td>1044</td>
<td>Key City Roller Derby</td>
<td>Key City</td>
<td>Womens</td>
<td>.30728</td>
</tr>
<tr>
<td><b>982</b></td>
<td>1045</td>
<td>Lindsay Roller Derby</td>
<td>Lindsay</td>
<td>Womens</td>
<td>.30702</td>
</tr>
<tr>
<td><b>983</b></td>
<td>1046</td>
<td>Sandusky Rollergirls</td>
<td>Sandusky</td>
<td>Womens</td>
<td>.30696</td>
</tr>
<tr>
<td><b>984</b></td>
<td>1047</td>
<td>Les Gueuses de Pigalle B</td>
<td>Les Gueuses A</td>
<td>Womens</td>
<td>.30691</td>
</tr>
<tr>
<td><b>985</b></td>
<td>1048</td>
<td>Redcliff Roller Derby Association</td>
<td>Redcliff</td>
<td>Womens</td>
<td>.30656</td>
</tr>
<tr>
<td><b>986</b></td>
<td>1049</td>
<td>Roller Derby Torino</td>
<td>Torino</td>
<td>Womens</td>
<td>.30649</td>
</tr>
<tr>
<td><b>987</b></td>
<td>1050</td>
<td>La Barbaque</td>
<td>Quads de Paris</td>
<td>Womens</td>
<td>.30624</td>
</tr>
<tr>
<td><b>988</b></td>
<td>1051</td>
<td>Plymouth City Roller Derby</td>
<td>Plymouth</td>
<td>Womens</td>
<td>.30622</td>
</tr>
<tr>
<td><b>989</b></td>
<td>1052</td>
<td>Brawlers</td>
<td>Hard Knox</td>
<td>Womens</td>
<td>.30600</td>
</tr>
<tr>
<td><b>990</b></td>
<td>1053</td>
<td>Castres Roller Derby</td>
<td>Castres</td>
<td>Womens</td>
<td>.30583</td>
</tr>
<tr>
<td><b>991</b></td>
<td>1054</td>
<td>Diamond State Rollergirls</td>
<td>Diamond State</td>
<td>Womens</td>
<td>.30552</td>
</tr>
<tr>
<td><b>992</b></td>
<td>1055</td>
<td>Van Diemen Rollers</td>
<td>Van Diemen</td>
<td>Womens</td>
<td>.30550</td>
</tr>
<tr>
<td><b>993</b></td>
<td>1056</td>
<td>Two Rivers Roller Derby B Team</td>
<td>Two Rivers</td>
<td>Womens</td>
<td>.30472</td>
</tr>
<tr>
<td><b>994</b></td>
<td>1057</td>
<td>Queen's Court</td>
<td>Queen City</td>
<td>Womens</td>
<td>.30459</td>
</tr>
<tr>
<td><b>995</b></td>
<td>1058</td>
<td>Narbonne Roller Sports</td>
<td>Head Hunters</td>
<td>Womens</td>
<td>.30457</td>
</tr>
<tr>
<td><b>996</b></td>
<td>1059</td>
<td>MidState Mayhem Roller Derby</td>
<td>MidState Mayhem</td>
<td>Womens</td>
<td>.30456</td>
</tr>
<tr>
<td><b>997</b></td>
<td>1060</td>
<td>Rebel Alliance</td>
<td>Melbourne Northside</td>
<td>Womens</td>
<td>.30415</td>
</tr>
<tr>
<td><b>998</b></td>
<td>1061</td>
<td>Black Thunders Madrid (Women's)</td>
<td>Black Thunders</td>
<td>Womens</td>
<td>.30405</td>
</tr>
<tr>
<td><b>999</b></td>
<td>1062</td>
<td>Wheels of Pain</td>
<td>Ohio Valley</td>
<td>Womens</td>
<td>.30380</td>
</tr>
<tr>
<td><b>1000</b></td>
<td>1063</td>
<td>Roller Derby Chalon</td>
<td>Roller Derby Chalon</td>
<td>Womens</td>
<td>.30376</td>
</tr>
<tr>
<td><b>1001</b></td>
<td>1064</td>
<td>Macomb Bombshells</td>
<td>Macomb</td>
<td>Womens</td>
<td>.30360</td>
</tr>
<tr>
<td><b>1002</b></td>
<td>1065</td>
<td>Roller Derby Palermo</td>
<td>Poison Kittens</td>
<td>Womens</td>
<td>.30318</td>
</tr>
<tr>
<td><b>1003</b></td>
<td>1066</td>
<td>Central California Area Derby</td>
<td>Central California</td>
<td>Womens</td>
<td>.30194</td>
</tr>
<tr>
<td><b>1004</b></td>
<td>1067</td>
<td>A-Town Roller Derby</td>
<td>A-Town</td>
<td>Womens</td>
<td>.30181</td>
</tr>
<tr>
<td><b>1005</b></td>
<td>1068</td>
<td>Arctic Roller Derby</td>
<td>Arctic</td>
<td>Womens</td>
<td>.30085</td>
</tr>
<tr>
<td><b>1006</b></td>
<td>1069</td>
<td>VooDoo Roller Dollies</td>
<td>Voodoo Roller Dollies</td>
<td>Womens</td>
<td>.30040</td>
</tr>
<tr>
<td><b>1007</b></td>
<td>1070</td>
<td>Lothian Derby Dolls</td>
<td>Lothian</td>
<td>Womens</td>
<td>.30033</td>
</tr>
<tr>
<td><b>1008</b></td>
<td>1071</td>
<td>Roller Derby La Rochelle</td>
<td>La Rochelle</td>
<td>Womens</td>
<td>.29988</td>
</tr>
<tr>
<td><b>1009</b></td>
<td>1072</td>
<td>Evolution Roller Derby</td>
<td>Evolution</td>
<td>Womens</td>
<td>.29966</td>
</tr>
<tr>
<td><b>1010</b></td>
<td>1073</td>
<td>Portside Pirates</td>
<td>Fog City</td>
<td>Womens</td>
<td>.29891</td>
</tr>
<tr>
<td><b>1011</b></td>
<td>1074</td>
<td>Darwin Rollergirls</td>
<td>Darwin</td>
<td>Womens</td>
<td>.29876</td>
</tr>
<tr>
<td><b>1012</b></td>
<td>1075</td>
<td>Hellfire Harlots B Team</td>
<td>Nottingham Hellfire Harlots</td>
<td>Womens</td>
<td>.29807</td>
</tr>
<tr>
<td><b>1013</b></td>
<td>1076</td>
<td>Ladies' Death and Derby Society</td>
<td>Ladies D&amp;D Society</td>
<td>Womens</td>
<td>.29675</td>
</tr>
<tr>
<td><b>1014</b></td>
<td>1077</td>
<td>Zombie Rollergirlz Münster</td>
<td>Münster</td>
<td>Womens</td>
<td>.29658</td>
</tr>
<tr>
<td><b>1015</b></td>
<td>1078</td>
<td>Ypsilanti Vigilantes</td>
<td>Ann Arbor</td>
<td>Womens</td>
<td>.29644</td>
</tr>
<tr>
<td><b>1016</b></td>
<td>1079</td>
<td>Preston Roller Girls B Team</td>
<td>Preston</td>
<td>Womens</td>
<td>.29611</td>
</tr>
<tr>
<td><b>1017</b></td>
<td>1080</td>
<td>Grimshaw Grim Reapers Roller Derby Team</td>
<td>Grimshaw</td>
<td>Womens</td>
<td>.29597</td>
</tr>
<tr>
<td><b>1018</b></td>
<td>1081</td>
<td>The Bad Seeds</td>
<td>Stuttgart Valley</td>
<td>Womens</td>
<td>.29551</td>
</tr>
<tr>
<td><b>1019</b></td>
<td>1082</td>
<td>Plan B</td>
<td>State College</td>
<td>Womens</td>
<td>.29530</td>
</tr>
<tr>
<td><b>1020</b></td>
<td>1083</td>
<td>GrassRoots Rollergirls</td>
<td>GrassRoots</td>
<td>Womens</td>
<td>.29522</td>
</tr>
<tr>
<td><b>1021</b></td>
<td>1084</td>
<td>Cheshire Hellcats Roller Derby</td>
<td>Cheshire</td>
<td>Womens</td>
<td>.29514</td>
</tr>
<tr>
<td><b>1022</b></td>
<td>1085</td>
<td>Bradentucky Bombers</td>
<td>Bradentucky</td>
<td>Womens</td>
<td>.29498</td>
</tr>
<tr>
<td><b>1023</b></td>
<td>1086</td>
<td>Les Petroleuses</td>
<td>Caen</td>
<td>Womens</td>
<td>.29483</td>
</tr>
<tr>
<td><b>1024</b></td>
<td>1087</td>
<td>Backlash</td>
<td>Punishers</td>
<td>Womens</td>
<td>.29473</td>
</tr>
<tr>
<td><b>1025</b></td>
<td>1088</td>
<td>Southern Maryland Roller Derby</td>
<td>Southern Maryland</td>
<td>Womens</td>
<td>.29439</td>
</tr>
<tr>
<td><b>1026</b></td>
<td>1089</td>
<td>Oisans Roller Derby</td>
<td>Les Sc'Alpes Hell</td>
<td>Womens</td>
<td>.29437</td>
</tr>
<tr>
<td><b>1027</b></td>
<td>1090</td>
<td>Roller Derby Côte Basque</td>
<td>Côte Basque</td>
<td>Womens</td>
<td>.29434</td>
</tr>
<tr>
<td><b>1028</b></td>
<td>1091</td>
<td>Ardèche rollers girl</td>
<td>Ardèche</td>
<td>Womens</td>
<td>.29352</td>
</tr>
<tr>
<td><b>1029</b></td>
<td>1092</td>
<td>Aurora Boriellas Roller Derby</td>
<td>Aurora Boriellas</td>
<td>Womens</td>
<td>.29305</td>
</tr>
<tr>
<td><b>1030</b></td>
<td>1093</td>
<td>Peoria Push Derby Dames</td>
<td>Peoria Push</td>
<td>Womens</td>
<td>.29245</td>
</tr>
<tr>
<td><b>1031</b></td>
<td>1094</td>
<td>Wicomikazis</td>
<td>Salisbury</td>
<td>Womens</td>
<td>.29209</td>
</tr>
<tr>
<td><b>1032</b></td>
<td>1095</td>
<td>Roller Skating Montreuil</td>
<td>Montreuil</td>
<td>Womens</td>
<td>.29185</td>
</tr>
<tr>
<td><b>1033</b></td>
<td>1096</td>
<td>Mankato Area Derby Girls</td>
<td>Mankato</td>
<td>Womens</td>
<td>.29173</td>
</tr>
<tr>
<td><b>1034</b></td>
<td>1097</td>
<td>The Banshees</td>
<td>South Sea</td>
<td>Womens</td>
<td>.29146</td>
</tr>
<tr>
<td><b>1035</b></td>
<td>1098</td>
<td>Palmetto State Rollergirls</td>
<td>Palmetto State</td>
<td>Womens</td>
<td>.29089</td>
</tr>
<tr>
<td><b>1036</b></td>
<td>1099</td>
<td>New Hampshire Roller Derby Cherry Bombs</td>
<td>New Hampshire</td>
<td>Womens</td>
<td>.29088</td>
</tr>
<tr>
<td><b>1037</b></td>
<td>1100</td>
<td>Broome County Rollers</td>
<td>BC Rollers</td>
<td>Womens</td>
<td>.28922</td>
</tr>
<tr>
<td><b>1038</b></td>
<td>1101</td>
<td>Capital Brawlers</td>
<td>Canberra</td>
<td>Womens</td>
<td>.28869</td>
</tr>
<tr>
<td><b>1039</b></td>
<td>1102</td>
<td>Smitten Kittens</td>
<td>Confluence</td>
<td>Womens</td>
<td>.28751</td>
</tr>
<tr>
<td><b>1040</b></td>
<td>1103</td>
<td>Cannon Brawlers</td>
<td>Mason-Dixon</td>
<td>Womens</td>
<td>.28686</td>
</tr>
<tr>
<td><b>1041</b></td>
<td>1104</td>
<td>Warrin' Wrecking Dolls</td>
<td>Wrecking Dolls</td>
<td>Womens</td>
<td>.28677</td>
</tr>
<tr>
<td><b>1042</b></td>
<td>1105</td>
<td>Bombshell Battalion</td>
<td>Renegade</td>
<td>Womens</td>
<td>.28582</td>
</tr>
<tr>
<td><b>1043</b></td>
<td>1106</td>
<td>Ayrshire Roller Derby</td>
<td>Ayrshire</td>
<td>Womens</td>
<td>.28541</td>
</tr>
<tr>
<td><b>1044</b></td>
<td>1107</td>
<td>Otway Derby Dolls</td>
<td>Otway</td>
<td>Womens</td>
<td>.28528</td>
</tr>
<tr>
<td><b>1045</b></td>
<td>1108</td>
<td>Roller Derby Russia</td>
<td>St. Petersburg</td>
<td>Womens</td>
<td>.28458</td>
</tr>
<tr>
<td><b>1046</b></td>
<td>1109</td>
<td>Port City Roller Derby</td>
<td>Port City</td>
<td>Womens</td>
<td>.28435</td>
</tr>
<tr>
<td><b>1047</b></td>
<td>1110</td>
<td>Shipwreckers</td>
<td>Harbor City</td>
<td>Womens</td>
<td>.28374</td>
</tr>
<tr>
<td><b>1048</b></td>
<td>1111</td>
<td>Crucibelles</td>
<td>Sheffield</td>
<td>Womens</td>
<td>.28363</td>
</tr>
<tr>
<td><b>1049</b></td>
<td>1112</td>
<td>South Island Sirens Roller Derby League</td>
<td>South Island Sirens</td>
<td>Womens</td>
<td>.28326</td>
</tr>
<tr>
<td><b>1050</b></td>
<td>1113</td>
<td>Far North Derby DollZ</td>
<td>Far North</td>
<td>Womens</td>
<td>.28285</td>
</tr>
<tr>
<td><b>1051</b></td>
<td>1114</td>
<td>Gulf Coast Rollergirls</td>
<td>Lafitte's Ladies</td>
<td>Womens</td>
<td>.28220</td>
</tr>
<tr>
<td><b>1052</b></td>
<td>1115</td>
<td>Wagga Derby Dolls</td>
<td>Wagga</td>
<td>Womens</td>
<td>.28215</td>
</tr>
<tr>
<td><b>1053</b></td>
<td>1116</td>
<td>Central Vermont Roller Derby</td>
<td>Central VT Roller Derby</td>
<td>Womens</td>
<td>.28168</td>
</tr>
<tr>
<td><b>1054</b></td>
<td>1117</td>
<td>Backyard Bullies</td>
<td>Suburbia</td>
<td>Womens</td>
<td>.28068</td>
</tr>
<tr>
<td><b>1055</b></td>
<td>1118</td>
<td>Rebel Army Derby</td>
<td>Rebel Army</td>
<td>Womens</td>
<td>.27989</td>
</tr>
<tr>
<td><b>1056</b></td>
<td>1119</td>
<td>Party Crashers</td>
<td>Circle City</td>
<td>Womens</td>
<td>.27931</td>
</tr>
<tr>
<td><b>1057</b></td>
<td>1120</td>
<td>Les Pisseuses Malefiques</td>
<td>Les Pisseuses</td>
<td>Womens</td>
<td>.27929</td>
</tr>
<tr>
<td><b>1058</b></td>
<td>1121</td>
<td>Misdemeanors</td>
<td>Ft. Myers</td>
<td>Womens</td>
<td>.27889</td>
</tr>
<tr>
<td><b>1059</b></td>
<td>1122</td>
<td>Mid Atlantic Roller Derby</td>
<td>Mid Atlantic</td>
<td>Womens</td>
<td>.27852</td>
</tr>
<tr>
<td><b>1060</b></td>
<td>1123</td>
<td>Nottingham Roller Girls B</td>
<td>Nottingham</td>
<td>Womens</td>
<td>.27812</td>
</tr>
<tr>
<td><b>1061</b></td>
<td>1124</td>
<td>Reckoning</td>
<td>Texas</td>
<td>Womens</td>
<td>.27605</td>
</tr>
<tr>
<td><b>1062</b></td>
<td>1125</td>
<td>Rapid Assault</td>
<td>Grand Raggidy</td>
<td>Womens</td>
<td>.27546</td>
</tr>
<tr>
<td><b>1063</b></td>
<td>1126</td>
<td>Farmers</td>
<td>Durham (Canada)</td>
<td>Womens</td>
<td>.27478</td>
</tr>
<tr>
<td><b>1064</b></td>
<td>1127</td>
<td>Murder City Roller Girls</td>
<td>Murder City</td>
<td>Womens</td>
<td>.27455</td>
</tr>
<tr>
<td><b>1065</b></td>
<td>1128</td>
<td>Southshire Roller Derby</td>
<td>Southshire</td>
<td>Womens</td>
<td>.27391</td>
</tr>
<tr>
<td><b>1066</b></td>
<td>1129</td>
<td>Norn Iron Maidens</td>
<td>Belfast</td>
<td>Womens</td>
<td>.27381</td>
</tr>
<tr>
<td><b>1067</b></td>
<td>1130</td>
<td>Hervey Bay Rollerz</td>
<td>Hervey Bay</td>
<td>Womens</td>
<td>.27378</td>
</tr>
<tr>
<td><b>1068</b></td>
<td>1131</td>
<td>River Valley Rollergirls (AR)</td>
<td>Arkansas River Valley</td>
<td>Womens</td>
<td>.27361</td>
</tr>
<tr>
<td><b>1069</b></td>
<td>1132</td>
<td>West Kentucky Rockin' Rollers</td>
<td>West KY</td>
<td>Womens</td>
<td>.27333</td>
</tr>
<tr>
<td><b>1070</b></td>
<td>1133</td>
<td>East Vic Roller Derby</td>
<td>East Vic</td>
<td>Womens</td>
<td>.27317</td>
</tr>
<tr>
<td><b>1071</b></td>
<td>1134</td>
<td>GVA Roller Derby Girls</td>
<td>Geneva</td>
<td>Womens</td>
<td>.27265</td>
</tr>
<tr>
<td><b>1072</b></td>
<td>1135</td>
<td>Roller Derby Luzern</td>
<td>Luzern</td>
<td>Womens</td>
<td>.27242</td>
</tr>
<tr>
<td><b>1073</b></td>
<td>1136</td>
<td>Cajun Rollergirls</td>
<td>Cajun Rollergirls</td>
<td>Womens</td>
<td>.27199</td>
</tr>
<tr>
<td><b>1074</b></td>
<td>1137</td>
<td>WayWARDs</td>
<td>Western Australia</td>
<td>Womens</td>
<td>.27193</td>
</tr>
<tr>
<td><b>1075</b></td>
<td>1138</td>
<td>Roller Derby 72</td>
<td>Le Mans</td>
<td>Womens</td>
<td>.27161</td>
</tr>
<tr>
<td><b>1076</b></td>
<td>1139</td>
<td>Margaret River Roller Derby</td>
<td>Margaret River</td>
<td>Womens</td>
<td>.27145</td>
</tr>
<tr>
<td><b>1077</b></td>
<td>1140</td>
<td>La Bande à ta Mère</td>
<td>Lyonnaises</td>
<td>Womens</td>
<td>.27022</td>
</tr>
<tr>
<td><b>1078</b></td>
<td>1141</td>
<td>ThunderDoms</td>
<td>Dom City</td>
<td>Womens</td>
<td>.26892</td>
</tr>
<tr>
<td><b>1079</b></td>
<td>1142</td>
<td>Las Palmas Roller Derby</td>
<td>Las Palmas</td>
<td>Womens</td>
<td>.26799</td>
</tr>
<tr>
<td><b>1080</b></td>
<td>1143</td>
<td>Roller Derby Ísland</td>
<td>Iceland</td>
<td>Womens</td>
<td>.26785</td>
</tr>
<tr>
<td><b>1081</b></td>
<td>1144</td>
<td>Roller Derby Salamanca</td>
<td>Salamanca</td>
<td>Womens</td>
<td>.26773</td>
</tr>
<tr>
<td><b>1082</b></td>
<td>1145</td>
<td>Coffs Coast Derby Dolls</td>
<td>Coffs Coast</td>
<td>Womens</td>
<td>.26744</td>
</tr>
<tr>
<td><b>1083</b></td>
<td>1146</td>
<td>Deadly Viper Assassination Squad</td>
<td>Toronto</td>
<td>Womens</td>
<td>.26666</td>
</tr>
<tr>
<td><b>1084</b></td>
<td>1147</td>
<td>Northern Beaches Roller Girls</td>
<td>Northern Beaches</td>
<td>Womens</td>
<td>.26583</td>
</tr>
<tr>
<td><b>1085</b></td>
<td>1148</td>
<td>Bilbo Roller Derby</td>
<td>Bilbo</td>
<td>Womens</td>
<td>.26439</td>
</tr>
<tr>
<td><b>1086</b></td>
<td>1149</td>
<td>Les Succubes Roller Derby</td>
<td>Les Succubes</td>
<td>Womens</td>
<td>.26421</td>
</tr>
<tr>
<td><b>1087</b></td>
<td>1150</td>
<td>Riverdale Rollers</td>
<td>Riverdale</td>
<td>Womens</td>
<td>.26415</td>
</tr>
<tr>
<td><b>1088</b></td>
<td>1151</td>
<td>Druid City Dames</td>
<td>Druid City</td>
<td>Womens</td>
<td>.26401</td>
</tr>
<tr>
<td><b>1089</b></td>
<td>1152</td>
<td>The Auver'Niaks</td>
<td>Auver'Niaks</td>
<td>Womens</td>
<td>.26281</td>
</tr>
<tr>
<td><b>1090</b></td>
<td>1153</td>
<td>Dead Ringers</td>
<td>Twin City</td>
<td>Womens</td>
<td>.26278</td>
</tr>
<tr>
<td><b>1091</b></td>
<td>1154</td>
<td>Kassel Roller Derby</td>
<td>Kassel</td>
<td>Womens</td>
<td>.26214</td>
</tr>
<tr>
<td><b>1092</b></td>
<td>1155</td>
<td>UnBreakaBellas</td>
<td>Cologne</td>
<td>Womens</td>
<td>.26199</td>
</tr>
<tr>
<td><b>1093</b></td>
<td>1156</td>
<td>Kill Squad</td>
<td>Killamazoo</td>
<td>Womens</td>
<td>.26186</td>
</tr>
<tr>
<td><b>1094</b></td>
<td>1157</td>
<td>Bedfordshire Rollergirls</td>
<td>Bedfordshire</td>
<td>Womens</td>
<td>.26176</td>
</tr>
<tr>
<td><b>1095</b></td>
<td>1158</td>
<td>Rock 'n' Roller Derby Murcia</td>
<td>Rock 'n' Roller Derby Murcia</td>
<td>Womens</td>
<td>.26108</td>
</tr>
<tr>
<td><b>1096</b></td>
<td>1159</td>
<td>Ace Invaders</td>
<td>Coastal Assassins</td>
<td>Womens</td>
<td>.26098</td>
</tr>
<tr>
<td><b>1097</b></td>
<td>1160</td>
<td>Barbed Wire Betties</td>
<td>Barbed Wire Betties</td>
<td>Womens</td>
<td>.26045</td>
</tr>
<tr>
<td><b>1098</b></td>
<td>1161</td>
<td>Meatgrinders Bremen</td>
<td>Bremen</td>
<td>Womens</td>
<td>.26022</td>
</tr>
<tr>
<td><b>1099</b></td>
<td>1162</td>
<td>East Coast Cyclones</td>
<td>East Coast</td>
<td>Womens</td>
<td>.25982</td>
</tr>
<tr>
<td><b>1100</b></td>
<td>1163</td>
<td>Hawkesbury/Hills Area Roller Derby</td>
<td>Hawkesbury/Hills Area</td>
<td>Womens</td>
<td>.25905</td>
</tr>
<tr>
<td><b>1101</b></td>
<td>1164</td>
<td>Bone City Rollers</td>
<td>Bone City</td>
<td>Womens</td>
<td>.25899</td>
</tr>
<tr>
<td><b>1102</b></td>
<td>1165</td>
<td>Badass Beavers</td>
<td>Gothenburg</td>
<td>Womens</td>
<td>.25813</td>
</tr>
<tr>
<td><b>1103</b></td>
<td>1166</td>
<td>Deathrow Hull</td>
<td>Deathrow</td>
<td>Womens</td>
<td>.25810</td>
</tr>
<tr>
<td><b>1104</b></td>
<td>1167</td>
<td>Roller Derby des Nordiks de Touraine</td>
<td>Tours</td>
<td>Womens</td>
<td>.25728</td>
</tr>
<tr>
<td><b>1105</b></td>
<td>1168</td>
<td>Whenua Fatales Roller Derby League</td>
<td>Whenua Fatales</td>
<td>Womens</td>
<td>.25678</td>
</tr>
<tr>
<td><b>1106</b></td>
<td>1169</td>
<td>Pittsburgh East Roller Villains (Women's)</td>
<td>Pittsburgh East (W)</td>
<td>Womens</td>
<td>.25611</td>
</tr>
<tr>
<td><b>1107</b></td>
<td>1170</td>
<td>Sucker Punch Roller Derby</td>
<td>Nürnberg</td>
<td>Womens</td>
<td>.25576</td>
</tr>
<tr>
<td><b>1108</b></td>
<td>1171</td>
<td>All City Rollers</td>
<td>All City</td>
<td>Womens</td>
<td>.25531</td>
</tr>
<tr>
<td><b>1109</b></td>
<td>1172</td>
<td>Canadian Clubbers</td>
<td>Border City Brawlers</td>
<td>Womens</td>
<td>.25506</td>
</tr>
<tr>
<td><b>1110</b></td>
<td>1173</td>
<td>Uppsala Roller Derby</td>
<td>Uppsala</td>
<td>Womens</td>
<td>.25482</td>
</tr>
<tr>
<td><b>1111</b></td>
<td>1174</td>
<td>Brutal Belles</td>
<td>Cedar Rapids Rollergirls</td>
<td>Womens</td>
<td>.25452</td>
</tr>
<tr>
<td><b>1112</b></td>
<td>1175</td>
<td>Skagit Valley Roller Derby</td>
<td>Skagit Valley</td>
<td>Womens</td>
<td>.25402</td>
</tr>
<tr>
<td><b>1113</b></td>
<td>1176</td>
<td>The Dire Skates</td>
<td>Dire Skates</td>
<td>Womens</td>
<td>.25383</td>
</tr>
<tr>
<td><b>1114</b></td>
<td>1177</td>
<td>Galway City She Devils</td>
<td>Galway</td>
<td>Womens</td>
<td>.25362</td>
</tr>
<tr>
<td><b>1115</b></td>
<td>1178</td>
<td>Psyko'Quads SGS Roller Derby</td>
<td>Psyko'Quads</td>
<td>Womens</td>
<td>.25339</td>
</tr>
<tr>
<td><b>1116</b></td>
<td>1179</td>
<td>Orcet Roller Derby (Team B)</td>
<td>Orcet (Womens)</td>
<td>Womens</td>
<td>.25234</td>
</tr>
<tr>
<td><b>1117</b></td>
<td>1180</td>
<td>Revolution Roller Derby</td>
<td>Rolling Valkyries</td>
<td>Womens</td>
<td>.25218</td>
</tr>
<tr>
<td><b>1118</b></td>
<td>1181</td>
<td>Rimini Roller Derby</td>
<td>Stray Beez</td>
<td>Womens</td>
<td>.25206</td>
</tr>
<tr>
<td><b>1119</b></td>
<td>1182</td>
<td>The Night Terrors</td>
<td>RGA The Wreckoning</td>
<td>Womens</td>
<td>.25204</td>
</tr>
<tr>
<td><b>1120</b></td>
<td>1183</td>
<td>Limoges Roller Skating</td>
<td>Limoges</td>
<td>Womens</td>
<td>.25198</td>
</tr>
<tr>
<td><b>1121</b></td>
<td>1184</td>
<td>HARD B</td>
<td>Hulls Angels</td>
<td>Womens</td>
<td>.25161</td>
</tr>
<tr>
<td><b>1122</b></td>
<td>1185</td>
<td>Broadbarians</td>
<td>East Lansing</td>
<td>Womens</td>
<td>.25043</td>
</tr>
<tr>
<td><b>1123</b></td>
<td>1186</td>
<td>Chemical Valley Rollergirls</td>
<td>Chemical Valley</td>
<td>Womens</td>
<td>.25022</td>
</tr>
<tr>
<td><b>1124</b></td>
<td>1187</td>
<td>Municorns</td>
<td>Munich</td>
<td>Womens</td>
<td>.25002</td>
</tr>
<tr>
<td><b>1125</b></td>
<td>1188</td>
<td>Sin City Rollers</td>
<td>Sin City Rollers</td>
<td>Womens</td>
<td>.24829</td>
</tr>
<tr>
<td><b>1126</b></td>
<td>1189</td>
<td>Northshore Roller Derby</td>
<td>Northshore</td>
<td>Womens</td>
<td>.24828</td>
</tr>
<tr>
<td><b>1127</b></td>
<td>1190</td>
<td>Ketchikan Rain Forest Roller Girls</td>
<td>Ketchikan</td>
<td>Womens</td>
<td>.24804</td>
</tr>
<tr>
<td><b>1128</b></td>
<td>1191</td>
<td>Waterford City Viqueens</td>
<td>Waterford</td>
<td>Womens</td>
<td>.24704</td>
</tr>
<tr>
<td><b>1129</b></td>
<td>1192</td>
<td>Motor City Madames</td>
<td>Durham (Canada)</td>
<td>Womens</td>
<td>.24627</td>
</tr>
<tr>
<td><b>1130</b></td>
<td>1193</td>
<td>Les Passeuses Dâmes</td>
<td>Les Passeuses Dâmes</td>
<td>Womens</td>
<td>.24606</td>
</tr>
<tr>
<td><b>1131</b></td>
<td>1194</td>
<td>Shitty Village B-Pol</td>
<td>Oulu</td>
<td>Womens</td>
<td>.24562</td>
</tr>
<tr>
<td><b>1132</b></td>
<td>1195</td>
<td>Anjou Derby Girls</td>
<td>Anjou</td>
<td>Womens</td>
<td>.24440</td>
</tr>
<tr>
<td><b>1133</b></td>
<td>1196</td>
<td>Demolition Dolls Roller Derby</td>
<td>Cookeville</td>
<td>Womens</td>
<td>.24388</td>
</tr>
<tr>
<td><b>1134</b></td>
<td>1197</td>
<td>Kokomo City of Fists Roller Derby</td>
<td>Kokomo</td>
<td>Womens</td>
<td>.24341</td>
</tr>
<tr>
<td><b>1135</b></td>
<td>1198</td>
<td>Beat City Bedrockers</td>
<td>Hartford Area</td>
<td>Womens</td>
<td>.24305</td>
</tr>
<tr>
<td><b>1136</b></td>
<td>1199</td>
<td>New Town Roller Girls</td>
<td>New Town</td>
<td>Womens</td>
<td>.24285</td>
</tr>
<tr>
<td><b>1137</b></td>
<td>1200</td>
<td>Roll-On Derby</td>
<td>Roll-On</td>
<td>Womens</td>
<td>.24164</td>
</tr>
<tr>
<td><b>1138</b></td>
<td>1201</td>
<td>Orleans Roller Derby Team B</td>
<td>Orléans</td>
<td>Womens</td>
<td>.24096</td>
</tr>
<tr>
<td><b>1139</b></td>
<td>1202</td>
<td>Dirty Jersey Roller Derby</td>
<td>Dirty Jersey</td>
<td>Womens</td>
<td>.24026</td>
</tr>
<tr>
<td><b>1140</b></td>
<td>1203</td>
<td>Roller Derby Chambéry</td>
<td>Chambéry</td>
<td>Womens</td>
<td>.24011</td>
</tr>
<tr>
<td><b>1141</b></td>
<td>1204</td>
<td>Roller Derby A Coruña</td>
<td>A Coruña</td>
<td>Womens</td>
<td>.23970</td>
</tr>
<tr>
<td><b>1142</b></td>
<td>1205</td>
<td>Pair O' Dice City Rollers</td>
<td>Pair O' Dice</td>
<td>Womens</td>
<td>.23953</td>
</tr>
<tr>
<td><b>1143</b></td>
<td>1206</td>
<td>Les Petites Frappes</td>
<td>Lutece</td>
<td>Womens</td>
<td>.23834</td>
</tr>
<tr>
<td><b>1144</b></td>
<td>1207</td>
<td>Hostess City Hellions</td>
<td>Savannah</td>
<td>Womens</td>
<td>.23819</td>
</tr>
<tr>
<td><b>1145</b></td>
<td>1208</td>
<td>East Coast Derby Dolls</td>
<td>East Coast</td>
<td>Womens</td>
<td>.23780</td>
</tr>
<tr>
<td><b>1146</b></td>
<td>1209</td>
<td>Maniac Monsters Mainz</td>
<td>Maniac Monsters Mainz</td>
<td>Womens</td>
<td>.23607</td>
</tr>
<tr>
<td><b>1147</b></td>
<td>1210</td>
<td>Demolitia Derby Queens</td>
<td>Demolitia</td>
<td>Womens</td>
<td>.23559</td>
</tr>
<tr>
<td><b>1148</b></td>
<td>1211</td>
<td>Northumberland Roller Girls</td>
<td>Northumberland</td>
<td>Womens</td>
<td>.23542</td>
</tr>
<tr>
<td><b>1149</b></td>
<td>1212</td>
<td>Bridgend Roller Derby</td>
<td>Bridgend</td>
<td>Womens</td>
<td>.23537</td>
</tr>
<tr>
<td><b>1150</b></td>
<td>1213</td>
<td>Mid-Hudson Misfits</td>
<td>Mid-Hudson</td>
<td>Womens</td>
<td>.23501</td>
</tr>
<tr>
<td><b>1151</b></td>
<td>1214</td>
<td>Southern Belles Roller Derby</td>
<td>Southern Belles</td>
<td>Womens</td>
<td>.23410</td>
</tr>
<tr>
<td><b>1152</b></td>
<td>1215</td>
<td>North Pole</td>
<td>North Pole</td>
<td>Womens</td>
<td>.23261</td>
</tr>
<tr>
<td><b>1153</b></td>
<td>1216</td>
<td>Team Regional Victoria</td>
<td>Rolling Matildas</td>
<td>Womens</td>
<td>.23260</td>
</tr>
<tr>
<td><b>1154</b></td>
<td>1217</td>
<td>Atlantic Breakers B</td>
<td>Cornwall</td>
<td>Womens</td>
<td>.23240</td>
</tr>
<tr>
<td><b>1155</b></td>
<td>1218</td>
<td>Cape Girardeau Roller Derby</td>
<td>Cape Girardeau</td>
<td>Womens</td>
<td>.23152</td>
</tr>
<tr>
<td><b>1156</b></td>
<td>1219</td>
<td>Roller Derby Mâcon (Women's)</td>
<td>Bananas Clit</td>
<td>Womens</td>
<td>.23030</td>
</tr>
<tr>
<td><b>1157</b></td>
<td>1220</td>
<td>Peterborough Area Roller Dervy</td>
<td>PARDy</td>
<td>Womens</td>
<td>.23005</td>
</tr>
<tr>
<td><b>1158</b></td>
<td>1221</td>
<td>Hell's Orchard Roller Derby</td>
<td>First Settlement</td>
<td>Womens</td>
<td>.22966</td>
</tr>
<tr>
<td><b>1159</b></td>
<td>1222</td>
<td>The Team B'East</td>
<td>Strasbourg</td>
<td>Womens</td>
<td>.22918</td>
</tr>
<tr>
<td><b>1160</b></td>
<td>1223</td>
<td>Les Faucheuses</td>
<td>Rouen</td>
<td>Womens</td>
<td>.22641</td>
</tr>
<tr>
<td><b>1161</b></td>
<td>1224</td>
<td>Valley Valkyries</td>
<td>Tweed Valley</td>
<td>Womens</td>
<td>.22597</td>
</tr>
<tr>
<td><b>1162</b></td>
<td>1225</td>
<td>Dockyard Brawlers</td>
<td>Halifax</td>
<td>Womens</td>
<td>.22592</td>
</tr>
<tr>
<td><b>1163</b></td>
<td>1226</td>
<td>Roller Derby Besançon</td>
<td>Besançon</td>
<td>Womens</td>
<td>.22543</td>
</tr>
<tr>
<td><b>1164</b></td>
<td>1227</td>
<td>Cape Breton Roller Derby</td>
<td>Cape Breton</td>
<td>Womens</td>
<td>.22475</td>
</tr>
<tr>
<td><b>1165</b></td>
<td>1228</td>
<td>The Disloyalists</td>
<td>Kingston</td>
<td>Womens</td>
<td>.22299</td>
</tr>
<tr>
<td><b>1166</b></td>
<td>1229</td>
<td>Mac-Town Sugar Skulls</td>
<td>Mac-Town</td>
<td>Womens</td>
<td>.22175</td>
</tr>
<tr>
<td><b>1167</b></td>
<td>1230</td>
<td>Roller Derby Argenteuil</td>
<td>Argenteuil</td>
<td>Womens</td>
<td>.22027</td>
</tr>
<tr>
<td><b>1168</b></td>
<td>1231</td>
<td>CORD B Squad</td>
<td>Central Ohio</td>
<td>Womens</td>
<td>.21854</td>
</tr>
<tr>
<td><b>1169</b></td>
<td>1232</td>
<td>Prague City Roller Derby B</td>
<td>Prague</td>
<td>Womens</td>
<td>.21665</td>
</tr>
<tr>
<td><b>1170</b></td>
<td>1233</td>
<td>Belfast City Rockets</td>
<td>Belfast City</td>
<td>Womens</td>
<td>.21651</td>
</tr>
<tr>
<td><b>1171</b></td>
<td>1234</td>
<td>North Devon Roller Girls B Team</td>
<td>North Devon</td>
<td>Womens</td>
<td>.21624</td>
</tr>
<tr>
<td><b>1172</b></td>
<td>1236</td>
<td>North West Roller Derby</td>
<td>North West</td>
<td>Womens</td>
<td>.21476</td>
</tr>
<tr>
<td><b>1173</b></td>
<td>1237</td>
<td>Seinäjoki Roller Derby</td>
<td>Seinäjoki</td>
<td>Womens</td>
<td>.21200</td>
</tr>
<tr>
<td><b>1174</b></td>
<td>1238</td>
<td>Roller Derby Le Havre</td>
<td>Le Havre</td>
<td>Womens</td>
<td>.21111</td>
</tr>
<tr>
<td><b>1175</b></td>
<td>1239</td>
<td>Wharf City Rollers</td>
<td>Wharf City</td>
<td>Womens</td>
<td>.20974</td>
</tr>
<tr>
<td><b>1176</b></td>
<td>1240</td>
<td>Örebro Roller Derby</td>
<td>Örebro</td>
<td>Womens</td>
<td>.20854</td>
</tr>
<tr>
<td><b>1177</b></td>
<td>1241</td>
<td>Oslo Tiger City Beasts</td>
<td>Oslo</td>
<td>Womens</td>
<td>.20628</td>
</tr>
<tr>
<td><b>1178</b></td>
<td>1242</td>
<td>Easo Avengers Roller Derby</td>
<td>Easo Avengers</td>
<td>Womens</td>
<td>.20559</td>
</tr>
<tr>
<td><b>1179</b></td>
<td>1243</td>
<td>American Revolution Roller Derby</td>
<td>American Revolution</td>
<td>Womens</td>
<td>.20467</td>
</tr>
<tr>
<td><b>1180</b></td>
<td>1244</td>
<td>Bonebreakers Bern</td>
<td>Bern</td>
<td>Womens</td>
<td>.20456</td>
</tr>
<tr>
<td><b>1181</b></td>
<td>1245</td>
<td>Dollinquents</td>
<td>Capital City</td>
<td>Womens</td>
<td>.20409</td>
</tr>
<tr>
<td><b>1182</b></td>
<td>1246</td>
<td>Eerie Roller Girls</td>
<td>Eerie Roller Girls</td>
<td>Womens</td>
<td>.20392</td>
</tr>
<tr>
<td><b>1183</b></td>
<td>1247</td>
<td>Tours B team</td>
<td>Tours</td>
<td>Womens</td>
<td>.20383</td>
</tr>
<tr>
<td><b>1184</b></td>
<td>1248</td>
<td>Swan City Derby Dames</td>
<td>Swan City</td>
<td>Womens</td>
<td>.20229</td>
</tr>
<tr>
<td><b>1185</b></td>
<td>1249</td>
<td>Gold City Rollers</td>
<td>Gold City</td>
<td>Womens</td>
<td>.20221</td>
</tr>
<tr>
<td><b>1186</b></td>
<td>1250</td>
<td>Eastside Derby Girls</td>
<td>Eastside Derby</td>
<td>Womens</td>
<td>.20221</td>
</tr>
<tr>
<td><b>1187</b></td>
<td>1251</td>
<td>Blackland Rockin' K-Rollers</td>
<td>Blackland</td>
<td>Womens</td>
<td>.20204</td>
</tr>
<tr>
<td><b>1188</b></td>
<td>1252</td>
<td>REC League - Nantes</td>
<td>Nantes</td>
<td>Womens</td>
<td>.20134</td>
</tr>
<tr>
<td><b>1189</b></td>
<td>1253</td>
<td>Roller Derby Vigo</td>
<td>RDV</td>
<td>Womens</td>
<td>.20118</td>
</tr>
<tr>
<td><b>1190</b></td>
<td>1254</td>
<td>Mobile's Derby Darlings</td>
<td>Mobile</td>
<td>Womens</td>
<td>.19959</td>
</tr>
<tr>
<td><b>1191</b></td>
<td>1255</td>
<td>Little Steel Derby Girls</td>
<td>Little Steel Derby Girls</td>
<td>Womens</td>
<td>.19927</td>
</tr>
<tr>
<td><b>1192</b></td>
<td>1256</td>
<td>WestCo Derby</td>
<td>WestCo</td>
<td>Womens</td>
<td>.19923</td>
</tr>
<tr>
<td><b>1193</b></td>
<td>1257</td>
<td>Mortal Condate</td>
<td>Rennes</td>
<td>Womens</td>
<td>.19912</td>
</tr>
<tr>
<td><b>1194</b></td>
<td>1258</td>
<td>J-Town Roller Girls</td>
<td>Flood City Sirens</td>
<td>Womens</td>
<td>.19802</td>
</tr>
<tr>
<td><b>1195</b></td>
<td>1259</td>
<td>Norfolk County Roller Derby</td>
<td>Norfolk County</td>
<td>Womens</td>
<td>.19457</td>
</tr>
<tr>
<td><b>1196</b></td>
<td>1260</td>
<td>Albany Roller Derby League</td>
<td>Albany Roller Derby</td>
<td>Womens</td>
<td>.19296</td>
</tr>
<tr>
<td><b>1197</b></td>
<td>1261</td>
<td>Pink Peril Rollerderby</td>
<td>Pink Peril</td>
<td>Womens</td>
<td>.19204</td>
</tr>
<tr>
<td><b>1198</b></td>
<td>1262</td>
<td>Roller Derby Luxembourg</td>
<td>Luxembourg</td>
<td>Womens</td>
<td>.19076</td>
</tr>
<tr>
<td><b>1199</b></td>
<td>1263</td>
<td>Coventry Roller Derby</td>
<td>Coventry</td>
<td>Womens</td>
<td>.19020</td>
</tr>
<tr>
<td><b>1200</b></td>
<td>1264</td>
<td>The Royal Brigade</td>
<td>The Royal Army</td>
<td>Womens</td>
<td>.18800</td>
</tr>
<tr>
<td><b>1201</b></td>
<td>1265</td>
<td>Derailers</td>
<td>South Shore</td>
<td>Womens</td>
<td>.18754</td>
</tr>
<tr>
<td><b>1202</b></td>
<td>1266</td>
<td>Outrage</td>
<td>DuPage Derby</td>
<td>Womens</td>
<td>.18506</td>
</tr>
<tr>
<td><b>1203</b></td>
<td>1267</td>
<td>B Devils</td>
<td>Penn Jersey</td>
<td>Womens</td>
<td>.18429</td>
</tr>
<tr>
<td><b>1204</b></td>
<td>1268</td>
<td>Berlin Rollergirls</td>
<td>Berlin Rollergirls</td>
<td>Womens</td>
<td>.18354</td>
</tr>
<tr>
<td><b>1205</b></td>
<td>1269</td>
<td>Roe City Rollers</td>
<td>Roe City Rollers</td>
<td>Womens</td>
<td>.18315</td>
</tr>
<tr>
<td><b>1206</b></td>
<td>1270</td>
<td>Kapiti Coast Derby Collective</td>
<td>Kapiti Coast</td>
<td>Womens</td>
<td>.18072</td>
</tr>
<tr>
<td><b>1207</b></td>
<td>1271</td>
<td>Appalachian Iron Maidens</td>
<td>Appalachian Iron Maidens</td>
<td>Womens</td>
<td>.17901</td>
</tr>
<tr>
<td><b>1208</b></td>
<td>1272</td>
<td>Montgomery Roller Derby</td>
<td>Montgomery</td>
<td>Womens</td>
<td>.17777</td>
</tr>
<tr>
<td><b>1209</b></td>
<td>1273</td>
<td>Poison Apples Roller Derby</td>
<td>Poison Apples</td>
<td>Womens</td>
<td>.17525</td>
</tr>
<tr>
<td><b>1210</b></td>
<td>1274</td>
<td>Roller Derby Bretenoux Biars</td>
<td>Enragées</td>
<td>Womens</td>
<td>.16623</td>
</tr>
<tr>
<td><b>1211</b></td>
<td>1275</td>
<td>Karlstad Roller Derby</td>
<td>Karlstad</td>
<td>Womens</td>
<td>.15813</td>
</tr>
<tr>
<td><b>1212</b></td>
<td>1276</td>
<td>Valley of the Derby Dollinquents</td>
<td>Voodoo Dolls</td>
<td>Womens</td>
<td>.15160</td>
</tr>
<tr>
<td><b>1213</b></td>
<td>1277</td>
<td>Rocket Dolls Roller Derby Coimbra</td>
<td>Coimbra</td>
<td>Womens</td>
<td>.14728</td>
</tr>
<tr>
<td><b>1214</b></td>
<td>1278</td>
<td>BURDs</td>
<td>Uppsala</td>
<td>Womens</td>
<td>.13909</td>
</tr>
<tr>
<td><b>1215</b></td>
<td>1279</td>
<td>Roller Derby Palois</td>
<td>Pau</td>
<td>Womens</td>
<td>.13151</td>
</tr>
<tr>
<td><b>1216</b></td>
<td>1280</td>
<td>Roller Derby Rochefort</td>
<td>Rochefort</td>
<td>Womens</td>
<td>.12658</td>
</tr>
<tr>
<td><b>1217</b></td>
<td>1281</td>
<td>Wasa Roller Derby</td>
<td>Wasa</td>
<td>Womens</td>
<td>.12636</td>
</tr>
<tr>
<td><b>1218</b></td>
<td>1282</td>
<td>Rail City Rollers</td>
<td>Rail City</td>
<td>Womens</td>
<td>.12436</td>
</tr>
<tr>
<td><b>1219</b></td>
<td>1283</td>
<td>Rockabellas Roller Derby League</td>
<td>Rockabellas</td>
<td>Womens</td>
<td>.10354</td>
</tr>
<tr>
<td><b>1220</b></td>
<td>1284</td>
<td>Southern Harm Derby Dames</td>
<td>Southern Harm</td>
<td>Womens</td>
<td>.09721</td>
</tr>
<tr>
<td><b>1221</b></td>
<td>1285</td>
<td>Pori Rolling Brigade</td>
<td>Pori</td>
<td>Womens</td>
<td>.09234</td>
</tr>
<tr>
<td><b>1222</b></td>
<td>1286</td>
<td>Reynoldsville Rebel Rollers</td>
<td>Reynoldsville</td>
<td>Womens</td>
<td>.08957</td>
</tr>
<tr>
<td><b>1223</b></td>
<td>1287</td>
<td>Lisbon Grrrls Roller Derby</td>
<td>Lisbon</td>
<td>Womens</td>
<td>.04746</td>
</tr>
<tr>
<td><b>1224</b></td>
<td>1288</td>
<td>Silver Bridge Bruisers</td>
<td>Silver Bridge</td>
<td>Womens</td>
<td>.01293</td>
</tr>
</tbody>
</table>
[<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/5/">NEXT PAGE</a></strong>]

<!--nextpage-->

[<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/4/">CLICK HERE TO SKIP TO TOP OF WOMEN</a></strong>] [<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/6/">SKIP TO DISCUSSION</a></strong>]
<h2>Men's Derby International Rankings 1 October 2016</h2>
<table>
<tbody>
<tr>
<td>RANK</td>
<td>Global Rank</td>
<td>TEAM</td>
<td>League</td>
<td>Type</td>
<td>Rating</td>
</tr>
<tr>
<td><b>1</b></td>
<td>3</td>
<td>Saint Louis GateKeepers</td>
<td>St. Louis GateKeepers</td>
<td>Mens</td>
<td>.96254</td>
</tr>
<tr>
<td><b>2</b></td>
<td>8</td>
<td>Your Mom Men's Roller Derby</td>
<td>Your Mom</td>
<td>Mens</td>
<td>.90259</td>
</tr>
<tr>
<td><b>3</b></td>
<td>9</td>
<td>New York Shock Exchange</td>
<td>Shock Exchange</td>
<td>Mens</td>
<td>.89790</td>
</tr>
<tr>
<td><b>4</b></td>
<td>10</td>
<td>Texas Men's Roller Derby</td>
<td>Texas Men's</td>
<td>Mens</td>
<td>.88954</td>
</tr>
<tr>
<td><b>5</b></td>
<td>11</td>
<td>Bridgetown Roller Derby</td>
<td>Bridgetown</td>
<td>Mens</td>
<td>.88487</td>
</tr>
<tr>
<td><b>6</b></td>
<td>14</td>
<td>Puget Sound Outcast Derby</td>
<td>Puget Sound</td>
<td>Mens</td>
<td>.85328</td>
</tr>
<tr>
<td><b>7</b></td>
<td>21</td>
<td>Magic City Misfits</td>
<td>Misfits</td>
<td>Mens</td>
<td>.82157</td>
</tr>
<tr>
<td><b>8</b></td>
<td>22</td>
<td>The Vancouver Murder</td>
<td>Vancouver Murder</td>
<td>Mens</td>
<td>.82022</td>
</tr>
<tr>
<td><b>9</b></td>
<td>30</td>
<td>Victorian Vanguard</td>
<td>Vanguard</td>
<td>Mens</td>
<td>.78649</td>
</tr>
<tr>
<td><b>10</b></td>
<td>32</td>
<td>San Diego Aftershocks</td>
<td>Aftershocks</td>
<td>Mens</td>
<td>.78151</td>
</tr>
<tr>
<td><b>11</b></td>
<td>33</td>
<td>Mass Maelstrom Roller Derby</td>
<td>Mass Maelstrom</td>
<td>Mens</td>
<td>.78059</td>
</tr>
<tr>
<td><b>12</b></td>
<td>34</td>
<td>Sydney City SMASH Men's Roller Derby</td>
<td>Sydney City SMASH</td>
<td>Mens</td>
<td>.77455</td>
</tr>
<tr>
<td><b>13</b></td>
<td>41</td>
<td>Philadelphia Hooligans</td>
<td>Philly Hooligans</td>
<td>Mens</td>
<td>.75245</td>
</tr>
<tr>
<td><b>14</b></td>
<td>43</td>
<td>Tasmania Men's Roller Derby</td>
<td>Tasmania Men's</td>
<td>Mens</td>
<td>.74989</td>
</tr>
<tr>
<td><b>15</b></td>
<td>44</td>
<td>ThunderQuads Roller Derby Masculino</td>
<td>ThunderQuads</td>
<td>Mens</td>
<td>.74784</td>
</tr>
<tr>
<td><b>16</b></td>
<td>55</td>
<td>Denver Roller Derby (Men's)</td>
<td>Ground Control</td>
<td>Mens</td>
<td>.72672</td>
</tr>
<tr>
<td><b>17</b></td>
<td>59</td>
<td>Montreal Men's Roller Derby</td>
<td>Mont Royals</td>
<td>Mens</td>
<td>.72134</td>
</tr>
<tr>
<td><b>18</b></td>
<td>65</td>
<td>Varsity Derby League (Mens)</td>
<td>Capital Carnage</td>
<td>Mens</td>
<td>.71526</td>
</tr>
<tr>
<td><b>19</b></td>
<td>67</td>
<td>Tampa Bay Men's Roller Derby</td>
<td>Tampa Bay</td>
<td>Mens</td>
<td>.71142</td>
</tr>
<tr>
<td><b>20</b></td>
<td>80</td>
<td>Brisbane City-Rollers (Men's)</td>
<td>Brisbane Men's</td>
<td>Mens</td>
<td>.69639</td>
</tr>
<tr>
<td><b>21</b></td>
<td>89</td>
<td>Chinook City Roller Derby (Men's)</td>
<td>Reservoir Dogs</td>
<td>Mens</td>
<td>.68627</td>
</tr>
<tr>
<td><b>22</b></td>
<td>91</td>
<td>Minnesota Men's Roller Derby</td>
<td>Twin Cities Terrors</td>
<td>Mens</td>
<td>.67988</td>
</tr>
<tr>
<td><b>23</b></td>
<td>94</td>
<td>Tweed Valley Roller's (Men's)</td>
<td>Tweed Valley Men's</td>
<td>Mens</td>
<td>.67746</td>
</tr>
<tr>
<td><b>24</b></td>
<td>95</td>
<td>Race City Rebels</td>
<td>Race City</td>
<td>Mens</td>
<td>.67632</td>
</tr>
<tr>
<td><b>25</b></td>
<td>113</td>
<td>Drive-By City Rollers</td>
<td>Drive-By City</td>
<td>Mens</td>
<td>.65542</td>
</tr>
<tr>
<td><b>26</b></td>
<td>120</td>
<td>Light City Derby (Mens)</td>
<td>Light City</td>
<td>Mens</td>
<td>.64758</td>
</tr>
<tr>
<td><b>27</b></td>
<td>124</td>
<td>Collision Men's Derby</td>
<td>Collision</td>
<td>Mens</td>
<td>.64504</td>
</tr>
<tr>
<td><b>28</b></td>
<td>127</td>
<td>Lane County Concussion</td>
<td>Lane County</td>
<td>Mens</td>
<td>.64417</td>
</tr>
<tr>
<td><b>29</b></td>
<td>129</td>
<td>Capital District Men's Roller Derby</td>
<td>Trauma Authority</td>
<td>Mens</td>
<td>.64278</td>
</tr>
<tr>
<td><b>30</b></td>
<td>130</td>
<td>Sioux City Kornstalkers</td>
<td>Kornstalkers</td>
<td>Mens</td>
<td>.64228</td>
</tr>
<tr>
<td><b>31</b></td>
<td>133</td>
<td>Rock City Riot</td>
<td>Rock City Riot</td>
<td>Mens</td>
<td>.63976</td>
</tr>
<tr>
<td><b>32</b></td>
<td>137</td>
<td>Perth Men's Derby</td>
<td>Perth Men's</td>
<td>Mens</td>
<td>.63760</td>
</tr>
<tr>
<td><b>33</b></td>
<td>138</td>
<td>Toronto Men's Roller Derby</td>
<td>Toronto Men's</td>
<td>Mens</td>
<td>.63674</td>
</tr>
<tr>
<td><b>34</b></td>
<td>150</td>
<td>Bridgetown Brawlers</td>
<td>Bridgetown</td>
<td>Mens</td>
<td>.62702</td>
</tr>
<tr>
<td><b>35</b></td>
<td>156</td>
<td>Carolina Wreckingballs Derby Team</td>
<td>Wreckingballs</td>
<td>Mens</td>
<td>.62066</td>
</tr>
<tr>
<td><b>36</b></td>
<td>161</td>
<td>Austin Anarchy Men's Roller Derby</td>
<td>Austin Anarchy</td>
<td>Mens</td>
<td>.61633</td>
</tr>
<tr>
<td><b>37</b></td>
<td>174</td>
<td>Milwaukee Blitzdkrieg</td>
<td>Blitzdkrieg</td>
<td>Mens</td>
<td>.60315</td>
</tr>
<tr>
<td><b>38</b></td>
<td>177</td>
<td>Cincinnati Battering Rams Men's Roller Derby</td>
<td>Battering Rams</td>
<td>Mens</td>
<td>.59863</td>
</tr>
<tr>
<td><b>39</b></td>
<td>180</td>
<td>Oklahoma City Wolf Pack</td>
<td>OKC Wolf Pack</td>
<td>Mens</td>
<td>.59702</td>
</tr>
<tr>
<td><b>40</b></td>
<td>193</td>
<td>B-Keepers</td>
<td>St. Louis GateKeepers</td>
<td>Mens</td>
<td>.58600</td>
</tr>
<tr>
<td><b>41</b></td>
<td>202</td>
<td>BisMan Roller Derby (Men's)</td>
<td>Bomberz</td>
<td>Mens</td>
<td>.58093</td>
</tr>
<tr>
<td><b>42</b></td>
<td>221</td>
<td>Mountain State Cutthroat Mafia</td>
<td>Uinta</td>
<td>Mens</td>
<td>.56953</td>
</tr>
<tr>
<td><b>43</b></td>
<td>222</td>
<td>Men's Ottawa Roller Derby</td>
<td>Slaughter Squad</td>
<td>Mens</td>
<td>.56943</td>
</tr>
<tr>
<td><b>44</b></td>
<td>232</td>
<td>Arizona Men's Derby</td>
<td>Rattleskates</td>
<td>Mens</td>
<td>.56400</td>
</tr>
<tr>
<td><b>45</b></td>
<td>262</td>
<td>Big O Roller Bros</td>
<td>Big O</td>
<td>Mens</td>
<td>.54734</td>
</tr>
<tr>
<td><b>46</b></td>
<td>274</td>
<td>Casco Bay Gentlemen's Derby</td>
<td>Casco Bay</td>
<td>Mens</td>
<td>.53769</td>
</tr>
<tr>
<td><b>47</b></td>
<td>275</td>
<td>Capital City Hooligans</td>
<td>Cap City Hooligans</td>
<td>Mens</td>
<td>.53767</td>
</tr>
<tr>
<td><b>48</b></td>
<td>312</td>
<td>New Orleans Brass Roller Derby</td>
<td>New Orleans Brass</td>
<td>Mens</td>
<td>.52199</td>
</tr>
<tr>
<td><b>49</b></td>
<td>316</td>
<td>Chicago Bruise Brothers</td>
<td>Bruise Brothers</td>
<td>Mens</td>
<td>.52056</td>
</tr>
<tr>
<td><b>50</b></td>
<td>366</td>
<td>Eastern Washington Wasteland Warriors</td>
<td>Eastern Washington</td>
<td>Mens</td>
<td>.50560</td>
</tr>
<tr>
<td><b>51</b></td>
<td>382</td>
<td>Atlanta Men's Roller Derby</td>
<td>Atlanta Men's</td>
<td>Mens</td>
<td>.49728</td>
</tr>
<tr>
<td><b>52</b></td>
<td>385</td>
<td>Detroit Men's Roller Derby</td>
<td>Detroit Riot</td>
<td>Mens</td>
<td>.49656</td>
</tr>
<tr>
<td><b>53</b></td>
<td>390</td>
<td>Quadfathers Men's Roller Derby</td>
<td>Quadfathers</td>
<td>Mens</td>
<td>.49449</td>
</tr>
<tr>
<td><b>54</b></td>
<td>392</td>
<td>Tulsa Derby Militia</td>
<td>Tulsa Derby Militia</td>
<td>Mens</td>
<td>.49401</td>
</tr>
<tr>
<td><b>55</b></td>
<td>404</td>
<td>Pittsburgh East Roller Villains (Men's)</td>
<td>Pittsburgh East (M)</td>
<td>Mens</td>
<td>.49028</td>
</tr>
<tr>
<td><b>56</b></td>
<td>407</td>
<td>Shenanigans</td>
<td>Philly Hooligans</td>
<td>Mens</td>
<td>.48959</td>
</tr>
<tr>
<td><b>57</b></td>
<td>443</td>
<td>Harm City Men's Derby</td>
<td>Harm City</td>
<td>Mens</td>
<td>.47726</td>
</tr>
<tr>
<td><b>58</b></td>
<td>448</td>
<td>Jersey Boys Roller Derby</td>
<td>Jersey Boys</td>
<td>Mens</td>
<td>.47591</td>
</tr>
<tr>
<td><b>59</b></td>
<td>534</td>
<td>Cleveland Men's Roller Derby</td>
<td>Cleveland Men's</td>
<td>Mens</td>
<td>.44680</td>
</tr>
<tr>
<td><b>60</b></td>
<td>646</td>
<td>Flour City Fear Men's Roller Derby</td>
<td>Flour City</td>
<td>Mens</td>
<td>.41392</td>
</tr>
<tr>
<td><b>61</b></td>
<td>675</td>
<td>Brigade of Handsome Gentlemen</td>
<td>Handsome Gentlemen</td>
<td>Mens</td>
<td>.40651</td>
</tr>
<tr>
<td><b>62</b></td>
<td>696</td>
<td>Kalamazoo Men's Roller Derby</td>
<td>Kalamazoo Men's</td>
<td>Mens</td>
<td>.40115</td>
</tr>
<tr>
<td><b>63</b></td>
<td>709</td>
<td>Men's Roller Derby of Kentucky</td>
<td>Kentucky Men's</td>
<td>Mens</td>
<td>.39684</td>
</tr>
<tr>
<td><b>64</b></td>
<td>1235</td>
<td>Northern Ontario Roller Derby</td>
<td>NORD Men's</td>
<td>Mens</td>
<td>.21519</td>
</tr>
</tbody>
</table>
[<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/3/">CLICK HERE TO GO TO COMBINED LIST</a></strong>][<strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/4/">CLICK HERE FOR WOMEN'S LIST</a></strong>]

<a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/6/"><strong>Next page</strong></a>, we'll have a bit more discussion!

<!--nextpage-->

In deference to the importance of the second largest grouping of Roller Derby leagues, representing the entirety of Men's Derby in Europe, we also present the ranking for that group. (Of course, <b>no absolute comparisons</b> between this ranking and the above are possible, as no bouts have taken place between the two in the past year).
<table>
<tbody>
<tr>
<td>EURO RANK</td>
<td>Team</td>
<td>EURO Rating</td>
</tr>
<tr>
<td><b>1</b></td>
<td>Southern Discomfort Roller Derby</td>
<td>1.00000</td>
</tr>
<tr>
<td><b>2</b></td>
<td>Tyne &amp; Fear Roller Derby</td>
<td>.77336</td>
</tr>
<tr>
<td><b>3</b></td>
<td>Lincolnshire Rolling Thunder</td>
<td>.75715</td>
</tr>
<tr>
<td><b>4</b></td>
<td>South Wales Silures</td>
<td>.76506</td>
</tr>
<tr>
<td><b>5</b></td>
<td>Manchester Roller Derby (Men's)</td>
<td>.74850</td>
</tr>
<tr>
<td><b>6</b></td>
<td>Roller Derby Toulouse (Men's)</td>
<td>.69283</td>
</tr>
<tr>
<td><b>7</b></td>
<td>South German Men's Roller Derby</td>
<td>.74003</td>
</tr>
<tr>
<td><b>8</b></td>
<td>Barrow Infernos</td>
<td>.67308</td>
</tr>
<tr>
<td><b>9</b></td>
<td>Panam Squad</td>
<td>.63250</td>
</tr>
<tr>
<td><b>10</b></td>
<td>Rouen Roller Derby (Men's)</td>
<td>.64258</td>
</tr>
<tr>
<td><b>11</b></td>
<td>Les Jules Vnres - Men's Roller Derby from Loire-Atlantique</td>
<td>.55237</td>
</tr>
<tr>
<td><b>12</b></td>
<td>The Mons'ter Munch Derby Dudes</td>
<td>.54225</td>
</tr>
<tr>
<td><b>13</b></td>
<td>Montpellier Derby Club (Men's)</td>
<td>.49173</td>
</tr>
<tr>
<td><b>14</b></td>
<td>Track'Ass (Men's)</td>
<td>.48758</td>
</tr>
<tr>
<td><b>15</b></td>
<td>Roller Derby Association</td>
<td>.46750</td>
</tr>
<tr>
<td><b>16</b></td>
<td>Orcet Roller Derby Wolfgang</td>
<td>.45595</td>
</tr>
<tr>
<td><b>17</b></td>
<td>S.T.Y.X Roller Derby Men Bordeaux</td>
<td>.43087</td>
</tr>
<tr>
<td><b>18</b></td>
<td>Manneken Beasts</td>
<td>.45963</td>
</tr>
<tr>
<td><b>19</b></td>
<td>Thugly Ducklings</td>
<td>.42543</td>
</tr>
<tr>
<td><b>20</b></td>
<td>Les Calebrutes de Montmartre</td>
<td>.40368</td>
</tr>
<tr>
<td><b>21</b></td>
<td>The Inhuman League</td>
<td>.44298</td>
</tr>
<tr>
<td><b>22</b></td>
<td>Suffolk Roller Derby (Men's)</td>
<td>.49831</td>
</tr>
<tr>
<td><b>23</b></td>
<td>Rotterdam Classy Cockroaches</td>
<td>.38248</td>
</tr>
<tr>
<td><b>24</b></td>
<td>Madrid MadRiders</td>
<td>.38312</td>
</tr>
<tr>
<td><b>25</b></td>
<td>Roller Derby Calaisis (Men's)</td>
<td>.36613</td>
</tr>
<tr>
<td><b>26</b></td>
<td>Inglorious Bstars</td>
<td>.38928</td>
</tr>
<tr>
<td><b>27</b></td>
<td>Crash Test Brummies</td>
<td>.38586</td>
</tr>
<tr>
<td><b>28</b></td>
<td>Roller Derby Mcon</td>
<td>.34151</td>
</tr>
<tr>
<td><b>29</b></td>
<td>Men's Roller Derby Grenoble</td>
<td>.31928</td>
</tr>
<tr>
<td><b>30</b></td>
<td>Wirral's Men's Roller Derby Team</td>
<td>.34089</td>
</tr>
<tr>
<td><b>31</b></td>
<td>Les Damns</td>
<td>.25253</td>
</tr>
<tr>
<td><b>32</b></td>
<td>Nottingham Super Smash Brollers</td>
<td>.28272</td>
</tr>
<tr>
<td><b>33</b></td>
<td>Teesside Skate Invaders</td>
<td>.25367</td>
</tr>
<tr>
<td><b>34</b></td>
<td>Roller Derby Dijon (Men's)</td>
<td>.22761</td>
</tr>
<tr>
<td><b>35</b></td>
<td>Milton Keynes Men's Roller Derby</td>
<td>.26520</td>
</tr>
<tr>
<td><b>36</b></td>
<td>Bairn City Rollers (Men's)</td>
<td>.25711</td>
</tr>
<tr>
<td><b>37</b></td>
<td>Mean City Roller Derby (Men's)</td>
<td>.17849</td>
</tr>
<tr>
<td><b>38</b></td>
<td>Kings of Block 'n' Roll</td>
<td>.19160</td>
</tr>
<tr>
<td><b>39</b></td>
<td>Nottingham Outlaws Roller Derby</td>
<td>.15274</td>
</tr>
<tr>
<td><b>40</b></td>
<td>Knights of Oldham Roller Derby</td>
<td>.18018</td>
</tr>
<tr>
<td><b>41</b></td>
<td>Capital City Roller Derby</td>
<td>.14319</td>
</tr>
<tr>
<td><b>42</b></td>
<td>Bristol Roller Derby (Men's)</td>
<td>.06357</td>
</tr>
<tr>
<td><b>43</b></td>
<td>Brawls of Steel</td>
<td>.17073</td>
</tr>
<tr>
<td><b>44</b></td>
<td>The Brothers Grim</td>
<td>.14984</td>
</tr>
<tr>
<td><b>45</b></td>
<td>East Anglo Smacksons</td>
<td>.13583</td>
</tr>
<tr>
<td><b>46</b></td>
<td>Medway Mayhem Roller Derby</td>
<td>.12207</td>
</tr>
<tr>
<td><b>47</b></td>
<td>Granite City Brawlers</td>
<td>.10108</td>
</tr>
<tr>
<td><b>48</b></td>
<td>Sons of Icarus</td>
<td>.06722</td>
</tr>
<tr>
<td><b>49</b></td>
<td>Aire Force 1</td>
<td>0</td>
</tr>
</tbody>
</table>
Of course, as the <strong><a href="http://www.flattrackstats.com">Flat Track Stats</a> </strong>dataset contains the entire history of (revival) Roller Derby, we can compute historical data using our ranking too. We ran 60 hours of calculation generating historical rankings for the past 8 years, to show how the community has evolved over time. As our ranking is normalised, the best team is always at 1, and the worst near 0 - in order to show how absolute performance has changed, we also show the underlying, non-normalised, rankings below.

<img class="alignnone size-full wp-image-9223" src="/2016/10/mw7rating.png" alt="mw7rating" width="640" height="480"> History of the final International Ranking, year on year (each year calculated for the 12 months up to 1 October that year).

 

<img class="alignnone size-full wp-image-9222" src="/2016/10/mw5ranking.png" alt="mw5ranking" width="640" height="480"> History of the unnormalised log Score Ratio component of the ranking, year on year. The peak value is a measure of the "spread" in ability within the group that sampling period.

<img class="alignnone size-full wp-image-9221" src="/2016/10/mw3ranking.png" alt="mw3ranking" width="640" height="480"> History of the unnormalised Score Difference component of the ranking, year on year. The peak value is a measure of the "spread" in ability within the group that sampling period.

As should be clear, the "peak ability" in Roller Derby increases fairly reliably year on year. As new teams enter the ranking mostly near the bottom, we believe that most of this increase in peak ability is actually due to the top teams getting better (as this is a relative ranking, it would also be possible for everyone else to be getting worse). We estimate, then, that (relative to the worst, "just starting out" leagues), the WFTDA/MRDA Top 10 leagues have increased their effective ability by a factor of 49!† (from the Score Ratio metric).

On the <strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/7/">next page</a></strong>, we'll compare our results to what WFTDA and Flat Track Stats have.

*We're working on a refinement, to be added in our next table update, to allow "ghost" rankings representative of leagues who drop out of the connected group between ranking calculation periods.

† From the Score Ratio metric, difference between absolute maximum of metric for 2008 and 2016.

<!--nextpage-->
<h2>Comparison with other rankings.</h2>
Much was made by <a href="https://medium.com/thederbyapex/the-sept-30th-rankings-rundown-d5021d962b0#.pv7iyc1zp"><strong>The Apex</strong> </a>that Angel City Roller Derby had "broken into the top 4" in the October WFTDA rankings. That this was a surprise perhaps reflects on an over concern with WFTDA's ranking system - for some time, Flat Track Stats had shown Angel City as superior to London (or even Rose) in strength, and our own internal rankings have also suggested this since March this year. It's not so much that Angel have suddenly gotten better - it's that WFTDA's addition of Decay to their metric is finally reflecting Angel's actual strength. [Observers of our <strong><a href="https://aoanla.wordpress.com/2016/09/27/ranking-mechanisms-from-sport-and-roller-derby/2/">stats comparison article</a></strong> will see that Angel are in the Top 4 for almost all rankings!]

<a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/3/"><strong>Our ranking</strong></a>, <strong><a href="https://www.wftda.com/rankings">WFTDA's</a></strong> and the <a href="http://flattrackstats.com/rankings"><strong>Flat Track Stats ranking</strong> </a>are all pretty good ranking schemes, even though they have slightly different aims, so we can perhaps gain something by looking at where they differ (they agree surprisingly well, which is a good signal for all of them).

Comparing to FTS's WFTDA ranking, and our Women Only, and with reference to The Apex's "talking points"...

<strong>Angel City... </strong>joins the Top 4 in WFTDA, but for both us and FTS, they're in the Top 3! In fact, FTS and us both agree that the Top 5 is Gotham, Victorian, <em>Angel</em>, London, Rose, with VRDL very close on Gotham (and statistically inseparable, in our ranking).
<p id="1356" class="graf graf--h4 graf-after--p"><strong>The Euros Are Coming...</strong> and how! FTS is more skeptical about Crime City than we and WFTDA are (placing them 17th to WFTDA's 13 and our 14), but whilst all three rankings agree that Rainy City Roller Derby deserves around 21st place, both FTS and us believe that Stockholm, Helsinki, and Kallio are even stronger than WFTDA places them. In fact, Middlesborough Milk Rollers and Paris Rollergirls are also both in our <em>Top 40</em>, in a strong point of disagreement with both of the more conservative rankings.</p>
<p class="graf graf--h4 graf-after--p"><strong>BAD's Basement... </strong>we agree with The Apex that they're about as low as they're likely to go... but not with WFTDA as to how low that is (we and FTS both place them at 18th, rather than 20th).</p>
<p id="3e01" class="graf graf--h4 graf-after--p"><strong>Biggest Mover ...</strong> we all differ on "new entrant" 2X4 Roller Derby. Whilst WFTDA has them with an impressive entry at #40, FTS is even more impressed, crediting them at #33... but our metric is somewhat less impressed, placing them at an impressive, but less astonishing 67. Remember, though, that our ranking includes non WFTDA leagues, and non A Teams, so some of those additional spots are taken by teams which just don't appear in the other two rankings.</p>
<p class="graf graf--h4 graf-after--p"><strong>The Euros Are Coming Pt 2...</strong> as previously mentioned, we rate Paris and MMR even more highly than WFTDA does, placing them in our Top 40! We agree that Leeds, Tiger Bay, Dublin and Newcastle are all very worthy Top 80 teams... and might add Lille and Bear City to that list (with Auld Reekie just a smidge outside at 83). Surprisingly, FTS is a bit more skeptical about several of these teams, placing, for example, Newcastle down in the 100s spots!</p>
<p id="ff5a" class="graf graf--h4 graf-after--p"><strong>The D2 Champs Teams Are All Under Ranked </strong>... The Apex believes that Calgary (@48), Brandywine (@50) , Charlottesville (@52) and Blue Ridge (@43) are all underranked by WFTDA.  FTS would mostly agree, placing Calgary@32, Brandywine@38 and Charlottesville@41, with Blue Ridge down at 47. On the other hand, our ranking (again, with the caveat that we are starting to include non WFTDA A teams at this level) disagrees, placing Calgary@55, Brandywine@56, Charlottesville@59 and Blue Ridge down at 62! In fact, the one thing that FTS and we seem to strongly agree on here is that Blue Ridge is <em>over</em>-ranked, compared to the other three!</p>
<p class="graf graf--h4 graf-after--p">On the <strong><a href="https://www.scottishrollerderbyblog.com/posts/2016/10/08/ranking-the-world-and-other-fts-visualisations/8/">next page</a></strong>, we'll cap things off with something a bit more fun.</p>
<!--nextpage-->
<h1>The Globe</h1>
Recently, it has become somewhat fashionable to present results in Roller Derby in the form of a Globe.

As the Flat Track Stats dataset records the geographical location of each league, we can easily use the Google Maps Geolocation API to programmatically look-up the coordinates of each league, and plot their rank on a globe. Anyone who wants the resulting dataset should feel free to contact us. (We're using a modified version of the Google Data Art's Team's WebGL globe, available here: <a href="https://github.com/dataarts/webgl-globe/">https://github.com/dataarts/webgl-globe/</a> for our visualisation.)

Due to some (security-related) restrictions on the content of Wordpress pages, our Globe Visualiser is hosted on our remote site, previously used for MRDWC2016's updates.
If the visualiser does not appear to work, please ensure that your web browser is not blocking JavaScript, and has "hardware acceleration" or "WebGL" enabled as an option.

<strong><a href="https://aoanla.pythonanywhere.com/globe.html">Link to The GLOBE: https://aoanla.pythonanywhere.com/globe.html</a></strong>

 </body></html>
