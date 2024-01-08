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

## Request the Data
We welcome collaborations from researchers of all academic fields interested in working with the German Academic Web.

Tell us what data you would like to work on and we will create and curate it.

Contact us via [E-Mail](mailto:robert.jaeschke@hu-berlin.de?subject=GAW Request).

## What
The German Academic Web (GAW) is a collection of snapshots of the public web presence of German academic institutions. The snapshots have been taken on a semi-annual basis since 2012 and contain web pages, which are stored in the [WARC](https://en.wikipedia.org/wiki/Web_ARChive)-format. These web pages contain a variety of information ranging from institution-wide announcements, CVs, course material pages, information about research projects or outgoing hyperlinks, as well as the message exchange (request-response meta data).

Each of the snapshots includes around 100 million breadth-first crawled web pages amounting to about 6-8 TB each comprising of text, PDF, image data. 

More information is available in the following paper:

Michael Paris and Robert Jäschke.\\
How to Assess the Exhaustiveness of Longitudinal Web Archives: A Case Study of the German Academic Web.\\
31st ACM Conference on Hypertext and Social Media (HT ’20).\\
DOI: [10.1145/3372923.3404836](https://doi.org/10.1145/3372923.3404836)

## Why
While there are institutions like the [Internet Archive](https://www.archive.org), which provide access to and preserve the history of the Web on a grand scale, a detailed image of domain specific regions is not provided. On a more granular level, many national libraries archive the top-level domains of their respective countries (e.g. [Deutsche Nationalbibliothek](https://www.dnb.de/DE/Professionell/Sammeln/Sammlung_Websites/sammlung_websites_node.html), [Bibliothèque nationale de France](https://www.bnf.fr/fr/archives-de-linternet), [National Library of Australia](https://trove.nla.gov.au/help/categories/websites-category)). 
Often, the scope of these web archives does not cover the content of the web sites exhaustively, leaving underlying regions unaccounted for. Such an operation requires an additional thematic focus to limit the magnitude of the regions to be archived. In these cases smaller players such as the [National Taiwan University Web Archiving System](http://webarchive.lib.ntu.edu.tw/eng/aboutus.asp), [Columbia University Web Archive](https://library.cumc.columbia.edu/node/2241) and ourselves step in to provide a highly detailed and topic specific web archive. 

See also [List of Web archiving initiatives](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives) for a survey of participants.

In conjunction with other datasets such as [GEPRIS (Geförderte Projekte Informationssystem)](https://gepris.dfg.de/gepris/) or [dblp](https://dblp.org/) we aim to investigate the temporal changes, time dependence of staff community structures and various improvement of NLP-tasks, such as entity-linking.

The GAW aims to preserve the evolution of the academic landscape's representaiton on the web. For one the knowledge published online by academic institutions might not be available or preserved for future scientific study. Further, there might be room for historical, sociological, psychological, informetric or scientometric studies as well as the exploration of the microskopic entities underlying these disciplines (e.g. trends in accessibiltity, public presentation, web development, organisational, staff or linguisitic shifts). 


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

<img src="https://amor.cms.hu-berlin.de/~tieslers/gaw/progress.svg" alt="Crawl progress">

## Dissemination
Here we list publications and other works utilizing the GAW dataset:

Michael Paris and Robert Jäschke.\\
How to Assess the Exhaustiveness of Longitudinal Web Archives: A Case Study of the German Academic Web.\\
31st ACM Conference on Hypertext and Social Media (HT ’20).\\
DOI: [10.1145/3372923.3404836](https://doi.org/10.1145/3372923.3404836)

Younes, Y., Tiesler, S., Jäschke, R., Mathiak, B.\\
Where are the Datasets? A case study on the German Academic Web Archive.\\
Proceedings of the Web Archiving and Digital Libraries Workshop at JCDL, 2022.
## About
The project is in part supported by the German Federal Ministry of Education and Research (BMBF) in the [REGIO](https://www.regio-project.org/) project (grant no. 01PU17012D).

<a href="https://www.regio-project.org/"><img src="/assets/images/logo/regio.svg" alt="REGIO" /></a>

### Team
 
[Prof. Dr. Robert Jäschke](https://www.ibi.hu-berlin.de/de/ueber-uns/personen/jaeschke)

Sebastian Tiesler

Jonathan Lüpfert

Michael Paris

Lars Ganser

[Information Processing and Analytics research group](https://www.ibi.hu-berlin.de/en/research/Information-processing)

### Additional Support by <a href="https://www.l3s.de/en"><img src="/assets/images/logo/L3S_Logo_NEU_small.jpg" alt="L3S"  style ="width: 10%; height: auto;" /></a>
