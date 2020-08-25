---
layout: article
title: German Academic Web OpenData
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

## what
The German Academic Web OpenData is a collection of snapshots of German academic institutions consisting of semiannual web crawls from 2012 onwards.

Each of the snapshots includes around 100 million crawled web pages amounting to about 6-8 TB each.

## why
While there are institutions like the [Internet Archive](https://www.archive.org), which provide access to and preserve the history of the Web on a grand scheme, a detailed image of domain specific regions can not be attained to a degree necessary for research. Here, smaller players step and provide a variety of web archives such as (hier zwei Beispiele und uns (UK oder US University, etwas exotisches)). (Erwähne und motiviere das Ziel, zeitliche Auflösung, science studies, web development, accessibiltity, conformity to standards (mit Quellen), structuring of unstructured data, improvement of NLP through knowledge graph infused learning, temporal search, tracing of researcher migration etc).

The curated corpus of German academic institution website snapshots reflects the evolution of scientific progress and communication and aims to make the data easily accessible for academic research.

## how
To get snapshots of the German Academic Web we crawl biannually in July and December all German academic institutions with the right to award doctorates as well as all institutions by the Fraunhofer and Max-Planck societies. The seeds are created new for every iteration and specific subsets, like source code management or e-learning platforms are excluded. (Hier könntest du auch etwas aus dem GAW Paper nehmen )

## dataset
The sets of crawled URLs including timestamps are available through in the Zenodo. For more information, see [Downloads](downloads.md).

<div class="flex-container">
    <div><a href="map.html"><img src="/assets/images/logo/uni_network.svg" style="width: 33%; height: auto;"><br>Map</a></div>
    <div><a href="basic_statistics.html"><img src="/assets/images/logo/bar-chart.svg" style="width: 33%; height: auto;"><br>Basic Statistics</a></div>
</div>

<div class="flex-container">
    <div><a href="universities.html"><img src="/assets/images/logo/iconfinder_238_bank_banking_online_university_building_education_3957679.svg" style="width: 50%; heigth: auto;"><br>Universities</a></div>
    <div><a href="mpis.html"><img src="/assets/images/logo/am_home-3373c950b109d16c9a5e494944afabe3.png" style="width: 50%; heigth: auto;"><br>Max-Planck</a></div>
    <div><a href="fhis.html"><img src="/assets/images/logo/fraunhofer_logo.svg" style="width: 50%; height: auto;" /><br>Fraunhofer</a></div>
</div>

## statistics

For more details, see [Statistics](basic_statistics.md).

### Latest Crawl

<img src="https://amor.cms.hu-berlin.de/~jaeschkr/crawler/progress.svg" alt="Crawl progress">


## data model and features
The crawled web pages are crawled by an instance of [Heritrix](https://www.github.com/internetarchive/heritrix3) and stored in Web ARChive archiving format, which are indexed in compact CDX index files.

## example usage
The content of the files may be processed by cluster-computing frameworks like [Apache Spark](https://spark.apache.org/). The corpus and derived data might be used for training of machine learning algorithms to answer research questions like:

- How do personal web pages on academic servers evolve?
- Can differences between departments regarding outside communication be determined regarding
  - the scientific community?
  - including citzens and opening up fields of science to the broader public?
- How prominent are different kinds of publications and/or presentations displayed?
- How connected are the different departments between institutions?
- Is an institution more focused on research or teaching?
  - Can we compute a score/metric based on different patterns discovered by machine learning algorithms?
- Can we find clusters of highly connected institutions?
- Are there central players in the German academic web?
- Has/had the excellence strategy an impact on the web presence?

## about
### team

[Prof. Dr. rer. nat. Robert Jäschke](https://www.ibi.hu-berlin.de/de/ueber-uns/personen/jaeschke)

[Michael Paris](https://www.ibi.hu-berlin.de/de/ueber-uns/personen/paris)

[Lars Ganser](https://www.ibi.hu-berlin.de/de/ueber-uns/personen/ganser)

[Information Processing and Analytics research group](https://www.ibi.hu-berlin.de/en/research/Information-processing)

### supported additionally by
<a href="https://www.regio-project.org/"><img src="/assets/images/logo/regio.svg" alt="REGIO" /></a>

<a href="https://www.l3s.de/en"><img src="/assets/images/logo/L3S_Logo_NEU_small.jpg" alt="L3S"  style ="width: 10%; height: auto;" /></a>
