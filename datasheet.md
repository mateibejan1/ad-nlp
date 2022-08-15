# AD-NLP Benchmark

By: [Matei Bejan] `<matei.bejan@s,unibuc.ro>` and [Andrei Manolache] `<amanolache@bitdefender.com>`

As part of a study making coreference systems more gender inclusive, we collected and annotated a dataset of documents by and about non-binary and binary trans people. We call this dataset the **Gender Inclusive Coreference (GICoref) dataset**; what follows below is the [datasheet](https://arxiv.org/abs/1803.09010) describing this data. If you use this dataset, please acknowledge it by citing the original paper:

```
@inproceedings{cao2019toward,
  title={AD-NLP: A Benchmark for Anomaly Detection in Natural Language Processing},
  author={Matei Bejan, Andrei Manolache and Marius Popescu},
  booktitle={Proceedings of the Conference of the Association for Computational Linguistics (ACL)},
  year={2022},
  note={}
}
```

## Motivation


1. **For what purpose was the dataset created?** *(Was there a specific task in mind? Was there a specific gap that needed to be filled? Please provide a description.)*
    
    The dataset was created as an extensive benchmark across multiple types of OOD data in NLP.


1. **Who created this dataset (e.g., which team, research group) and on behalf of which entity (e.g., company, institution, organization)?**
    
    This dataset was created by Matei Bejan, Andrei Manolache and Marius Popescu. At the time of the creation, Matei Bejan was a PhD Student at the University of Bucharest, Marius Popescu was an Associated Professor at the University of Bucharest, and Andrei Manolache was a Machine Learning Engineer at Bitdefender.


1. **Who funded the creation of the dataset?** *(If there is an associated grant, please provide the name of the grantor and the grant name and number.)*
    
    Project was partially funded by UEFISCDI, under Project PN-III-P2-2.1-PTE-2019-0532.


1. **Any other comments?**
    
    None.





## Composition


1. **What do the instances that comprise the dataset represent (e.g., documents, photos, people, countries)?** *(Are there multiple types of instances (e.g., movies, users, and ratings; people and interactions between them; nodes and edges)? Please provide a description.)*
    
    Each instance is composed of one or multiple English phrases, along with a corresponding annotation.

2. **How many instances are there in total (of each type, if appropriate)?**

    The benchmark holds a total of 172,917 train samples and 26,879 test samples and it is comprised of seven datasets from nine sources:

    * [The 20Newgroups dataset](http://qwone.com/~jason/20Newsgroups/).
    * [The AGNews dataset](http://groups.di.unipi.it/~gulli/AG_corpus_of_news_articles.html).
    * [The CoLA dataset](https://nyu-mll.github.io/CoLA/). 
    * [The VUA dataset](http://www.vismet.org/metcor/documentation/home.html). The data is annotated according to the MIPVU procedure as described by its authors. As a consequence, the words annotated as metaphors have been prefixed with the "M\_" string in the original annotation setting. In order to transform this initial problem setup of text segmentation into one of anomaly detection and for the data to comply with our methodology, we removed the word-level annotations and instead labeled the whole sentences as containing a metaphor or not.
    * [Project Gutenberg](https://www.gutenberg.org/). We scraped the entire website using a custom script to parse all bookshelves, which stored the book texts, their authors, and titles, as well as the category in which they were placed by Project Gutenberg. We annotated the books with respect to said category. The result is a [corpus of over 15,000 literary texts](https://www.kaggle.com/mateibejan/15000-gutenberg-books), along with their authors, titles, titles and bookshelves (a term that Gutenberg maintainers use for categories). We then filtered this dataset to produce **Gutenberg Categories** and **Gutenberg Authors**.
    * The last four sources have been used to construct the **Song Genres** dataset. We have labeled three out of the four datasets with a genre feature using the [spotipy](https://pypi.org/project/spotipy/) library, which uses the Spotify API in order to retrieve the genre of an Artist. The Spotify API returns a list of genres for one artist, so we consider the mode of that list to be the dominant genre of the lyrics of said artist. Additionally, we used the [langdetect](https://pypi.org/project/langdetect/) library to automatically label the lyrics with a language. In total, the lyrics come in 34 languages. They four sources are as follows:
        - 2018 Textract Hackathon. Data provided by Sparktech Software.
        - [150K Lyrics Labeled with Spotify Valence](https://www.kaggle.com/datasets/edenbd/150k-lyrics-labeled-with-spotify-valence).
        - [dataset lyrics musics](https://www.kaggle.com/datasets/italomarcelo/dataset-lyrics-musics).
        - [AZLyrics song lyrics](https://www.kaggle.com/datasets/albertsuarez/azlyrics).

    We have used the original versions of the classical datasets 20Newsgroups, AGNews, as well as CoLA and VUA. 
    
    For the newly-introduced Gutenberg Authors, Gutenberg Categories, we have selected 10 classes which we believed offer both intra and inter domain variety. We provide a list of said classes for eat dataset below.

    TODO: add list

    For the newly-introduced Song Genres, our labeling procedure automatically labels the data taken from `150K Lyrics Labeled with Spotify Valence`, `dataset lyrics musics and `AZLyrics song lyrics` with the labels present in the `2018 Textract Hackathon` data, namely: Pop, Hip-Hop, Rock, Metal, Folk, Jazz, Country, and Electronic.
    
    TODO: Add table with data statistics.

    | Source               | #Total   | #Train  | #Test | 
    | :---                 | :---:    | :---:   | :---: |    
    | 20Newsgroups         | 19,815   | 10,996  | 8819  | 
    | AGNews               | 127,600  | 120,000 | 7600  | 
    | CoLA                 | 9584     | 8551    | 1043  | 
    | VUA                  | 12,122   | 8485    | 3637  | 
    | Song Genres          | 18,900   | 15,120  | 3780  | 
    | Gutenberg Authors    | 6000     | 5000    | 1000  | 
    | Gutenberg Categories | 5765     | 4765    | 1000  | 
    | **TOTAL**            | **95**   | **70,614** | **6307** | **735** | **65** | **8.9%** |

3. **Does the dataset contain all possible instances or is it a sample (not necessarily random) of instances from a larger set?** *(If the dataset is a sample, then what is the larger set? Is the sample representative of the larger set (e.g., geographic coverage)? If so, please describe how this representativeness was validated/verified. If it is not representative of the larger set, please describe why not (e.g., to cover a more diverse range of instances, because instances were withheld or unavailable).)*
    
    The 20Newsgroups, AGNews, CoLA and VUA datasets have been used in their entirety. 
    The Gutenberg Authors and Gutenberg Categories datasets are a subset of the [15,000 Gutenberg Books](https://www.kaggle.com/datasets/mateibejan/15000-gutenberg-books) dataset, which consists of all scraped data from the Project Gutenberg website.
    The Song Genres dataset is a subset of the [Multi-Lingual Lyrics for Genre Classification](https://www.kaggle.com/datasets/mateibejan/multilingual-lyrics-for-genre-classification), which has hundreds of artists and dozens of languages.


4. **What data does each instance consist of?** *(``Raw'' data (e.g., unprocessed text or images)or features? In either case, please provide a description.)*
    
    Each instance consists of text that has been separated into one or multiple sentences, tokenized and cleaned.

5. **Is there a label or target associated with each instance? If so, please provide a description.**
    
    Each dataset is designated one directory, which contains train and test directories. These two directories contain multiple `txt` files. Each `txt` file represents one class. All samples of said class are written within that file. Samples are separated by two newline characters `\n\n`.

    An example of the dataset structure is provided below:
```
src
    ├── data                       
        ├── gutenberg_categories  
            ├── train               
                ├── Biology.txt
                ├── Canada.txt
                ├── CIA.txt
                ...
            ├── test
                ├── Biology.txt
                ├── Canada.txt
                ├── CIA.txt
                ...
    ├── ...

```

6. **Is any information missing from individual instances?** *(If so, please provide a description, explaining why this information is missing (e.g., because it was unavailable). This does not include intentionally removed information, but might include, e.g., redacted text.)*
    
    No information missing.


7. **Are relationships between individual instances made explicit (e.g., users' movie ratings, social network links)?** *( If so, please describe how these relationships are made explicit.)*
    
    No relationships between individual instances.


8. **Are there recommended data splits (e.g., training, development/validation, testing)?** *(If so, please provide a description of these splits, explaining the rationale behind them.)*
    
    We recommend the provided training/testing split, for reproductibility reasons.


9. **Are there any errors, sources of noise, or redundancies in the dataset?** *(If so, please provide a description.)*
    
    No errors or redundancies that we are aware of.

10. **Is the dataset self-contained, or does it link to or otherwise rely on external resources (e.g., websites, tweets, other datasets)?** *(If it links to or relies on external resources, a) are there guarantees that they will exist, and remain constant, over time; b) are there official archival versions of the complete dataset (i.e., including the external resources as they existed at the time the dataset was created); c) are there any restrictions (e.g., licenses, fees) associated with any of the external resources that might apply to a future user? Please provide descriptions of all external resources and any restrictions associated with them, as well as links or other access points, as appropriate.)*
    
    The benchmark is relies on external resources, which are as follows: the 20Newsgrous dataset, the AGNews dataset, the CoLA dataset and the VUA dataset. Given the importance of the former two as classical baselines in NLP and the latter two in their own respective fields, we believe that they will exist, and remain constant, over time.

    TODO: add licenses


11. **Does the dataset contain data that might be considered confidential (e.g., data that is protected by legal privilege or by doctor-patient confidentiality, data that includes the content of individuals' non-public communications)?** *(If so, please provide a description.)*
    
    No; all raw data in the dataset is from public sources (publicly available datasets, Project Gutenberg, Kaggle).


12. **Does the dataset contain data that, if viewed directly, might be offensive, insulting, threatening, or might otherwise cause anxiety?** *(If so, please describe why.)*
    
    No.

13. **Does the dataset relate to people?** *(If not, you may skip the remaining questions in this section.)*
    
    Some of the data, namely the news datasets (20Newsgroups and AGNews) relate to real people. Others, such as Gutenberg Authors and Gutenberg Categories partially contain data that related to real people, alongside fictional data. The Song Genres dataset contains lyrics inspired from real world interactions.


14. **Does the dataset identify any subpopulations (e.g., by age, gender)?** *(If so, please describe how these subpopulations are identified and provide a description of their respective distributions within the dataset.)*
    
    No, the benchmark does no contain any such data.

15. **Is it possible to identify individuals (i.e., one or more natural persons), either directly or indirectly (i.e., in combination with other data) from the dataset?** *(If so, please describe how.)*
    
    Yes, it is possible to identify authors and artists from the class names, as well as other people referenced throughout the texts.


16. **Does the dataset contain data that might be considered sensitive in any way (e.g., data that reveals racial or ethnic origins, sexual orientations, religious beliefs, political opinions or union memberships, or locations; financial or health data; biometric or genetic data; forms of government identification, such as social security numbers; criminal history)?** *(If so, please provide a description.)*
    
    The data does not reveal any such information, as far as we know.


17. **Any other comments?**
    
    None.





## Collection Process


1. **How was the data associated with each instance acquired?** *(Was the data directly observable (e.g., raw text, movie ratings), reported by subjects (e.g., survey responses), or indirectly inferred/derived from other data (e.g., part-of-speech tags, model-based guesses for age or language)? If data was reported by subjects or indirectly inferred/derived from other data, was the data validated/verified? If so, please describe how.)*
    
    The data was all downloaded directly from associated webpages (Wikipedia, periodicals, or AO3). Tokenization and sentence segmentation was initially done automatically but corrected by hand.


1. **What mechanisms or procedures were used to collect the data (e.g., hardware apparatus or sensor, manual human curation, software program, software API)?** *(How were these mechanisms or procedures validated?)*
    
    Annotation was conducted using [TagEditor](https://github.com/d5555/TagEditor).


1. **If the dataset is a sample from a larger set, what was the sampling strategy (e.g., deterministic, probabilistic with specific sampling probabilities)?**
    
    See answer to question #2 in [Composition](#composition).


1. **Who was involved in the data collection process (e.g., students, crowdworkers, contractors) and how were they compensated (e.g., how much were crowdworkers paid)?**
    
    All collection and annotation was done by the two authors.


1. **Over what timeframe was the data collected?** *(Does this timeframe match the creation timeframe of the data associated with the instances (e.g., recent crawl of old news articles)?  If not, please describe the timeframe in which the data associated with the instances was created.)*
    
    The dataset was collected in the early Summer of 2019, which does not necessarily reflect the timeframe of the data collected.


1. **Were any ethical review processes conducted (e.g., by an institutional review board)?** *(If so, please provide a description of these review processes, including the outcomes, as well as a link or other access point to any supporting documentation.)*
    
    No review processes were conducted with respect to the collection and annotation of this data (though review was done for other aspects of this work; see the paper linked at the top of the datasheet).


1. **Does the dataset relate to people?** *(If not, you may skip the remaining questions in this section.)*
    
    Yes; the majority of the documents in the dataset are articles about people (either their Wikipedia entries or stories about them in periodicals).


1. **Did you collect the data from the individuals in question directly, or obtain it via third parties or other sources (e.g., websites)?**
    
    Other sources: Wikipedia and periodicals.


1. **Were the individuals in question notified about the data collection?** *(If so, please describe (or show with screenshots or other information) how notice was provided, and provide a link or other access point to, or otherwise reproduce, the exact language of the notification itself.)*
    
    No, they were not notified.


1. **Did the individuals in question consent to the collection and use of their data?** *(If so, please describe (or show with screenshots or other information) how consent was requested and provided, and provide a link or other access point to, or otherwise reproduce, the exact language to which the individuals consented.)*
    
    No. All documents are public. In the case of the AO3 stories, we explicitly contacted the authors and received permission to use their stories. (Several authors we contacted did not respond; we did not include their stories.)


1. **If consent was obtained, were the consenting individuals provided with a mechanism to revoke their consent in the future or for certain uses?** *(If so, please provide a description, as well as a link or other access point to the mechanism (if appropriate).)*
    
    N/A.


1. **Has an analysis of the potential impact of the dataset and its use on data subjects (e.g., a data protection impact analysis) been conducted?** *(If so, please provide a description of this analysis, including the outcomes, as well as a link or other access point to any supporting documentation.)*
    
    No. 


1. **Any other comments?**
    
    None.





## Preprocessing/cleaning/labeling


1. **Was any preprocessing/cleaning/labeling of the data done (e.g., discretization or bucketing, tokenization, part-of-speech tagging, SIFT feature extraction, removal of instances, processing of missing values)?** *(If so, please provide a description. If not, you may skip the remainder of the questions in this section.)*
    
    Yes; the documents were truncated at 1000 words, sentence split and tokenized.


1. **Was the "raw" data saved in addition to the preprocessed/cleaned/labeled data (e.g., to support unanticipated future uses)?** *(If so, please provide a link or other access point to the "raw" data.)*
    
    Yes, the original raw data is included in the distribution, in the folder `raw`.


1. **Is the software used to preprocess/clean/label the instances available?** *(If so, please provide a link or other access point.)*
    
    Yes; it is [TagEditor](https://github.com/d5555/TagEditor) version 1.5.


1. **Any other comments?**
    
    None.





## Uses


1. **Has the dataset been used for any tasks already?** *(If so, please provide a description.)*
    
    The dataset has been used to understand human annotation biases and to test existing coreference systems. See the paper linked at the top for more details.


1. **Is there a repository that links to any or all papers or systems that use the dataset?** *(If so, please provide a link or other access point.)*
    
    No.


1. **What (other) tasks could the dataset be used for?**
    
    The dataset could possibly be used for developing or testing systems for referring expression generation. 


1. **Is there anything about the composition of the dataset or the way it was collected and preprocessed/cleaned/labeled that might impact future uses?** *(For example, is there anything that a future user might need to know to avoid uses that could result in unfair treatment of individuals or groups (e.g., stereotyping, quality of service issues) or other undesirable harms (e.g., financial harms, legal risks)  If so, please provide a description. Is there anything a future user could do to mitigate these undesirable harms?)*
    
    While the dataset was specifically constructed to be gender inclusive, it undoubtedly fails in some ways to full achieve that goal. Part of this is due to the nature of the underlying texts (eg, Wikipedia's frequent use of deadnames) and part of it is due to plain difficulties in collection (automatically distinguishing specific singular uses of "they" from other uses is currently not possible, and so despite "they" being currently, likely, the most commonly used non-binary pronoun, it is perhaps underrepresented in this dataset). Preprocessing hopefully did not introduce errors (in fact, we corrected for many tokenization errors, for instance, that the default tokenizer did not know to split "xe'll" into two tokens as it would "she'll").


1. **Are there tasks for which the dataset should not be used?** *(If so, please provide a description.)*
    
    This dataset should not be used for any sort of "gender prediction." First, anyone using this dataset (or any related dataset, for that matter), should recognize that "gender" doesn't mean any single thing, and furthermore that pronoun != gender. Furthermore, because of the fluid and temporal notion of gender--and of gendered referring expressions like pronouns and terms of address--just because a person is described in this dataset in one particular way, does not mean that this will always be the appropriate way to refer to this person.


2. **Any other comments?**
    
    None.




## Distribution


1. **Will the dataset be distributed to third parties outside of the entity (e.g., company, institution, organization) on behalf of which the dataset was created?** *(If so, please provide a description.)*
    
    Yes, the dataset is freely available.


1. **How will the dataset will be distributed (e.g., tarball  on website, API, GitHub)?** *(Does the dataset have a digital object identifier (DOI)?)*
    
    The dataset is free for download at github.com/hal3/gicoref-dataset.


1. **When will the dataset be distributed?**
    
    The dataset is distributed as of June 2020 in its first version.


1. **Will the dataset be distributed under a copyright or other intellectual property (IP) license, and/or under applicable terms of use (ToU)?** *(If so, please describe this license and/or ToU, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms or ToU, as well as any fees associated with these restrictions.)*
    
    The dataset is licensed under a BSD license.


1. **Have any third parties imposed IP-based or other restrictions on the data associated with the instances?** *(If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any relevant licensing terms, as well as any fees associated with these restrictions.)*
    
    Not to our knowledge.


1. **Do any export controls or other regulatory restrictions apply to the dataset or to individual instances?** *(If so, please describe these restrictions, and provide a link or other access point to, or otherwise reproduce, any supporting documentation.)*
    
    Not to our knowledge.


1. **Any other comments?**
    
    None.





## Maintenance


1. **Who is supporting/hosting/maintaining the dataset?**
    
    Both authors (Trista Cao and Hal Daumé III) are maintaining. Hal is hosting on github.


1. **How can the owner/curator/manager of the dataset be contacted (e.g., email address)?**
    
    E-mail addresses are at the top of this document.


1. **Is there an erratum?** *(If so, please provide a link or other access point.)*
    
    Currently, no. As errors are encountered, future versions of the dataset may be released (but will be versioned). They will all be provided in the same github location.


1. **Will the dataset be updated (e.g., to correct labeling errors, add new instances, delete instances')?** *(If so, please describe how often, by whom, and how updates will be communicated to users (e.g., mailing list, GitHub)?)*
    
    Same as previous.


1. **If the dataset relates to people, are there applicable limits on the retention of the data associated with the instances (e.g., were individuals in question told that their data would be retained for a fixed period of time and then deleted)?** *(If so, please describe these limits and explain how they will be enforced.)*
    
    No.


1. **Will older versions of the dataset continue to be supported/hosted/maintained?** *(If so, please describe how. If not, please describe how its obsolescence will be communicated to users.)*
    
    Yes; all data will be versioned.


1. **If others want to extend/augment/build on/contribute to the dataset, is there a mechanism for them to do so?** *(If so, please provide a description. Will these contributions be validated/verified? If so, please describe how. If not, why not? Is there a process for communicating/distributing these contributions to other users? If so, please provide a description.)*
    
    Errors may be submitted via the bugtracker on github. More extensive augmentations may be accepted at the authors' discretion.


1. **Any other comments?**
    
    None.


