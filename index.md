---
title: Home
layout: home
lang: en
description: A description of the German Academic Web dataset
---

# What
The German Academic Web (GAW) is a collection of snapshots of the
public web presence of German academic institutions. This comprises a
variety of information, for example, press releases, course material,
or legal documents (e.g., examination regulations) as well as
information about research projects and researchers.

The snapshots have been taken semi-annually since 2012 and are stored
as [WARC](https://en.wikipedia.org/wiki/Web_ARChive) files.  Each
snapshot includes around 100 million documents – mainly HTML pages,
images, and PDF files – amounting to about 6-8&nbsp;TB per snapshot.
The WARC files also document the HTTP message exchange
(request-response meta data) and the outgoing hyperlinks per HTML
page.

# Why
While institutions like the [Internet
Archive](https://www.archive.org/) provide access to and preserve the
history of the Web on a grand scale and many national libraries
archive the top-level domain of their respective country (e.g.,
[Deutsche
Nationalbibliothek](https://www.dnb.de/DE/Professionell/Sammeln/Sammlung_Websites/sammlung_websites_node.html),
[Bibliothèque nationale de
France](https://www.bnf.fr/fr/archives-de-linternet), [National
Library of
Australia](https://trove.nla.gov.au/help/categories/websites-category)),
their goal is seldom the exhaustive archiving of individual web sites
or regions of the Web. This requires an additional thematic focus to
limit the magnitude of the regions of the Web to be archived.  Smaller
institutions such as the [National Taiwan University Web Archiving
System](http://webarchive.lib.ntu.edu.tw/eng/aboutus.asp), [Columbia
University Web Archive](https://library.cumc.columbia.edu/node/2241)
and the GAW step in to provide highly detailed and topic-specific
archive of academic web pages (see also the [list of Web archiving
initiatives](https://en.wikipedia.org/wiki/List_of_Web_archiving_initiatives)).

With the GAW we aim to preserve the evolution of the academic
landscape by archiving its representation on the Web. This can enable
future historical, sociological, psychological, informetric, or
scientometric studies as well as the exploration of scholarly entities
(e.g., projects, institutions, researchers) and related aspects (e.g.,
trends in accessibility, public presentation, web development, as well
as organisational, staff, or linguistic changes).

# How
For each crawl a current version of
[Heritrix](https://github.com/internetarchive/heritrix3) (2012/10:
3.0.0, 2013/02-2015/12: 3.1.0, 2016/06-2020/12: 3.2.0, 2020/06-:
3.4.0) is initialised with a conceptually invariant seed list of, on
average, 150 domains of German academic institutions with the right to
award doctorates (extracted from [Liste der Hochschulen in
Deutschland](https://de.wikipedia.org/wiki/Liste_der_Hochschulen_in_Deutschland)).
In addition, institutes from the [Fraunhofer
Society](https://www.fraunhofer.de/) and the [Max-Planck
Society](https://mpg.de/) are included.

The crawler follows a breadth-first policy on each host, thereby
collecting all available pages reachable by links from the homepage as
deep as 20 hops. The scope is limited to crawl only pages from the
seed domains and certain file types (mainly audio, video, and
compressed files) are excluded using regular expressions.

During the crawl, the URL queues are monitored via a web UI. Hosts
that appear to be undesirable, such as e-learning systems or
repositories, are added to a list of 'retired' hosts, that is, their
URLs are no longer crawled in the running and future crawls. However,
previously harvested URLs from retired hosts are neither removed from
prior crawls nor from the running crawl.  As the operators learn over
time, there are constant adjustments to the configuration (e.g., crawl
delays, exclusion of hosts based on requests, etc.)

Most crawls were finished (manually) after approximately 100 million
pages were collected (according to Heritrix' control console), which
takes roughly two weeks per crawl.

The resulting web archive files conform to [ISO
28500:2009](https://www.iso.org/standard/44717.html) and compact CDX
index files are hosted in part by the [L3S](https://www.l3s.de/)
Research Center in Hannover, in part by the [Information Processing
and Analytics
group](https://www.ibi.hu-berlin.de/en/research/Information-processing).


# About
The project was in part supported by the German Federal Ministry of
Education and Research (BMBF) in the [REGIO
project](https://www.regio-project.org/) (grant no. 01PU17012D).

The crawl is operated and hosted by the [Information Processing and
Analytics
group](https://www.ibi.hu-berlin.de/en/research/Information-processing)
at [Humboldt-Universität zu Berlin](https://hu-berlin.de/):
- [Prof. Dr. Robert Jäschke](https://amor.cms.hu-berlin.de/~jaeschkr/)
- Sebastian Tiesler
- Jonathan Lüpfert
- Michael Paris
- Lars Ganser

# Datasets
The [lists of crawled URLs](downloads.md) including timestamps are
available through [Zenodo](https://zenodo.org/communities/regio).

We welcome collaboration requests from researchers of all academic
fields interested in working with the German Academic Web. [Contact
us](mailto:robert.jaeschke@hu-berlin.de?subject=GAW Request) and tell
us what data you would like to work on and we will see how we can
support you.

# Dissemination
Publications and other works utilizing the GAW dataset:
- Michael Paris and Robert Jäschke (2020). How to Assess the
  Exhaustiveness of Longitudinal Web Archives: A Case Study of the
  German Academic Web. *31st ACM Conference on Hypertext and Social
  Media (HT 2020).*
  doi:[10.1145/3372923.3404836](https://doi.org/10.1145/3372923.3404836)
- Younes, Y., Tiesler, S., Jäschke, R., Mathiak, B. (2022). Where are
  the Datasets? A case study on the German Academic Web
  Archive. *[Proceedings of the Web Archiving and Digital Libraries
  Workshop at JCDL, 2022.](http://hdl.handle.net/10919/114213)*
- Lisa Spindler (2022). Publikationsdaten auf Webseiten deutscher
  Forschungseinrichtungen: Eine Pilotstudie für die Analyse des German
  Academic Web. *Master thesis*, Fachhochschule Potsdam &
  Humboldt-Universität zu Berlin.
- Robert Jäschke (2023). Tales from the inside: 10 years of growing
  and maintaining a multi-terabyte longitudinal archive of web pages
  and tweets. *Workshop: Do It Yourself-Archives*, July 7, 2023,
  Potsdam, Germany.
- Plamena Neycheva (2024). Forschungsdatenwebseiten: eine
  Online-Inhaltsanalyse mit Schwerpunkt auf Metadaten. *Master
  thesis*, Humboldt-Universität zu Berlin.
  doi:[10.18452/33441](https://doi.org/10.18452/33441)
- Plamena Neycheva and Robert Jäschke (2025). 100 categorized URLs of
  web pages that describe, contain, or link to (research) datasets
  [Data set]. Zenodo.
  doi:[10.5281/zenodo.16418047](https://doi.org/10.5281/zenodo.16418047)

# Latest Crawl

![crawl progress](https://amor.cms.hu-berlin.de/~tieslers/gaw/progress.svg)
