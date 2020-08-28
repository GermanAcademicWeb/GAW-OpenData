---
layout: article
title: German Academic Web
lang: en
---
<head>
    <style>
        .flex-container {
            display: flex;
            justify-content: space-between;
            background-color: white;
        }
        .flex-container > div {
            background-color: white;
            width: 1000px;
            margin: 10px;
            text-align: center;
            line-height: 75px;
            font-size: 30px;
        }
    </style>
</head>

## What
The German Academic Web corpus is a collection of snapshots of the public web presence of German academic institutions consisting of semiannual web crawls from 2012 onwards. It contains a multitude of data ranging from institution-wide announcement statements to students to CVs of faculty, course material pages and descriptions of research projects.

Each of the snapshots includes around 100 million crawled web pages amounting to about 6-8 TB each comprising of text (including PDFs) and image data. 

More information is available at the following paper:

Michael Paris and Robert Jäschke.\\
How to Assess the Exhaustiveness of Longitudinal Web Archives: A Case Study of the German Academic Web.\\
31st ACM Conference on Hypertext and Social Media (HT ’20).\\
DOI: [10.1145/3372923.3404836](https://doi.org/10.1145/3372923.3404836)

## Request the Data
We welcome collaborations from researchers of all academic fields interested in working with our web data.

Tell us what data you would like to work on and we will create and curate it.

Contact us via [E-Mail](mailto:robert.jaeschke@hu-berlin.de?subject=GAW Request).

## Why
While there are institutions like the [Internet Archive](https://www.archive.org), which provide access to and preserve the history of the Web on a grand scheme, a detailed image of domain specific regions can not be attained to a degree necessary for research. On a more granular level many national archives crawl the respective top-level domain of the respective country (e.g. [Deutsche Nationalbibliothek](https://www.dnb.de/DE/Professionell/Sammeln/Sammlung_Websites/sammlung_websites_node.html), [Bibliothèque nationale de France](https://www.bnf.fr/fr/archives-de-linternet), [National Library of Australia](https://trove.nla.gov.au/help/categories/websites-category)). Alas the depth of the crawls is not sufficient for specific scientific fields and smaller players such as the [National Taiwan University Web Archiving System](http://webarchive.lib.ntu.edu.tw/eng/aboutus.asp), [Columbia University Web Archive](https://library.cumc.columbia.edu/node/2241) and we step in and provide a variety of web archives. 

See also [List of Web archiving initiatives](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives) for a survey of participants.

One the one hand knowledge published online by academic institutions might not be available or preserved for future scientific study. On the other hand there might be room for historical, sociological, psychological, informetrical or scientometrical studies of entities themselfes (e.g. trends in accessibiltity, public presentation, web development, organisational, staff or linguisitic shifts). In conjunction with datasets such as [GEPRIS (Geförderte Projekte Informationssystem)](https://gepris.dfg.de/gepris/) as structured foundation for example there are open chances for temporal search, community-detection in inter-personal relationships based on affiliations and tracing of researcher migration or in general improvement of NLP through knowledge graph infused learning as a foundation with much text material in German.

The curated corpus of semiannual German academic institution website snapshots aims to expand a knowledge base of the German academic web and offer a reflection of the evolution of scientific progress and communication and aims to make the data easily accessible for academic research.

## How

For each crawl a current version of [Heritrix](https://github.com/internetarchive/heritrix3) (2012/10: 3.0.0, 2013/02-2015/12: 3.1.0, 2016/06-2020/12: 3.2.0, 2020/06-: 3.4.0) is initialised with a conceptually invariant seed list of, on average, 150 domains of all German academic institutions with the right to award doctorates. The seed list is extracted from the current entries on [Liste der Hochschulen in Deutschland](https://de.wikipedia.org/wiki/Liste_der_Hochschulen_in_Deutschland). Fraunhofer and Max-Planck institutions are added manually by adding the general seeds *fraunhofer.de* and *mpg.de*.

The crawler follows a breadth-first policy on each host, thereby collecting all available pages reachable by links from the homepage as deep as 20 hops. The scope is limited to crawl only pages from the seed domains and certain file types (mainly audio, video, and compressed files) are excluded by a growing number of regular expressions. 

Along the crawl, the URL queues are monitored via a web UI. Hosts that appear to be undesirable, such as e-learning systems or repositories, are added to a growing list of 'retired' hosts, that is, their URLs are no longer crawled in the running and future crawls. However, previously harvested URLs from retired hosts are not removed from the running crawl.
As the operators learn over time, there are constant adjustments to the configuration (e.g. crawl delays, exclusion of hosts based on requests, etc.)

Most crawls were finished (manually) after roughly 100 million pages are collected (according to Heritrix' control console), which takes roughly two weeks per crawl, on average.

The resulting Web ARChive files conform to [ISO 28500:2009](https://www.iso.org/standard/44717.html) and compact CDX index files are hosted in part by the [L3S](https://www.l3s.de/) research center in Hannover, in part by Humboldt-Universität zu Berlin.

## Datasets
The sets of crawled URLs including timestamps are available through  in the Zenodo. For more information, see [Downloads](downloads.md).

<div class="flex-container">
    <div><a href="map.html"><img src="/assets/images/logo/uni_network.svg" style="width: 33%; height: auto;"><br>Map</a></div>
    <div><a href="basic_statistics.html"><img src="/assets/images/logo/bar-chart.svg" style="width: 33%; height: auto;"><br>Statistics</a></div>
</div>

<div class="flex-container">
    <div><a href="universities.html"><img src="/assets/images/logo/iconfinder_238_bank_banking_online_university_building_education_3957679.svg" style="width: 50%; heigth: auto;"><br>Universities</a></div>
    <div><a href="mpis.html"><img src="/assets/images/logo/am_home-3373c950b109d16c9a5e494944afabe3.png" style="width: 50%; heigth: auto;"><br>Max-Planck</a></div>
    <div><a href="fhis.html"><img src="/assets/images/logo/fraunhofer_logo.svg" style="width: 50%; height: auto;" /><br>Fraunhofer</a></div>
</div>

## Latest Crawl

<img src="https://amor.cms.hu-berlin.de/~jaeschkr/crawler/progress.svg" alt="Crawl progress">

## Sample Research Questions

- Is there an evolution of personal web pages on academic servers? And if yes, how can it be researched?
- What are differences between departments regarding outside communication:
  - scientific community?
  - open science?
  - citizen science?
- How prominent are different kinds of publications and/or presentations displayed?
- How connected are the different departments between institutions?
- Is an institution more focussed on research or teaching?
  - Can a score/metric based on different patterns discovered by machine learning algorithms be computed?
- Can clusters of highly connected institutions be identified?
- Are there central players in the German academic web?
- Had the excellence initiative or has the excellence strategy an impact on the web presence of universities?

- How did outside communication on web presences changed in the face of the COVID-19 pandemic?

## About
The project is in part supported by the German Federal Ministry of Education and Research (BMBF) in the [REGIO](https://www.regio-project.org/) project (grant no. 01PU17012D).

<a href="https://www.regio-project.org/"><img src="/assets/images/logo/regio.svg" alt="REGIO" /></a>

### Team
 
[Prof. Dr. rer. nat. Robert Jäschke](https://www.ibi.hu-berlin.de/de/ueber-uns/personen/jaeschke)

[Michael Paris](https://www.ibi.hu-berlin.de/de/ueber-uns/personen/paris)

[Lars Ganser](https://www.ibi.hu-berlin.de/de/ueber-uns/personen/ganser)

[Information Processing and Analytics research group](https://www.ibi.hu-berlin.de/en/research/Information-processing)

### Additional Support by <a href="https://www.l3s.de/en"><img src="/assets/images/logo/L3S_Logo_NEU_small.jpg" alt="L3S"  style ="width: 10%; height: auto;" /></a>
