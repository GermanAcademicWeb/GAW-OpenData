---
title: Statistics
layout: page
lang: en
---

# Basic Statistics

|    Date | No. of WARC Files | Data in TB | Start Time (UTC)    | End Time (UTC)      | WARC records |
| ------- | ----------------: | ---------: | ------------------- | ------------------- | -----------: |
| 2024-06 |              8816 |       8.00 | 2024-06-05 13:15:33 | 2024-06-19 09:19:10 | 100,672,853  |
| 2023-12 |              8675 |       7.90 | 2023-12-11 11:22:42 | 2023-12-25 10:54:45 | 101,769,884  |
| 2023-06 |              8614 |       7.84 | 2023-06-08 15:14:04 | 2023-06-20 08:17:33 | 100,402,845  |
| 2022-12 |              8122 |       7.40 | 2022-12-06 08:02:33 | 2022-12-17 20:06:41 | 102,954,813  |
| 2022-06 |              7855 |       7.20 | 2022-06-09 12:06:53 | 2022-06-20 10:25:27 | 101,420,390  |
| 2021-12 |              7202 |       6.56 | 2021-12-07 07:20:59 | 2021-12-17 07:07:08 | 101,919,655  |
| 2021-06 |              7207 |       6.57 | 2021-06-01 11:21:10 | 2021-06-14 06:33:25 | 105,563,149  |
| 2020-12 |              6998 |       6.37 | 2020-12-01 09:19:54 | 2020-12-10 07:58:47 | 100,269,671  |
| 2020-06 |              6953 |       6.41 | 2020-06-03 07:44:24 | 2020-06-11 11:44:55 | 99,999,403   |
| 2019-12 |              7035 |       6.41 | 2019-12-03 10:08:00 | 2019-12-10 11:32:52 | 100,976,809  |
| 2019-06 |              7012 |       6.39 | 2019-06-13 06:48:30 | 2019-06-27 11:07:40 | 99,797,675   |
| 2018-12 |              7297 |       6.65 | 2018-12-03 09:37:41 | 2018-12-14 22:32:14 | 100,768,903  |
| 2018-06 |              7106 |       6.47 | 2018-06-18 07:08:26 | 2018-06-29 21:31:07 | 101,022,822  |
| 2017-12 |              7374 |       6.72 | 2017-12-05 12:42:27 | 2017-12-17 10:17:47 | 102,133,168  |
| 2017-06 |              7417 |       6.76 | 2017-06-12 07:44:06 | 2017-06-21 07:09:56 | 100,847,532  |
| 2016-12 |              7088 |       6.46 | 2016-12-08 08:13:23 | 2016-12-17 12:15:04 | 99,952,250   |
| 2016-06 |              7289 |       6.64 | 2016-06-01 07:34:12 | 2016-06-13 07:01:58 | 112,824,260  |
| 2015-12 |              5928 |       5.40 | 2015-12-15 09:42:56 | 2016-01-05 07:40:02 | 101,279,483  |
| 2015-05 |              6449 |       5.87 | 2015-05-27 08:25:50 | 2015-06-09 06:04:34 | 103,575,494  |
| 2014-12 |              6154 |       5.60 | 2014-12-01 08:28:56 | 2014-12-08 06:01:53 | 100,145,401  |
| 2014-05 |              6339 |       5.77 | 2014-04-30 06:40:49 | 2014-05-13 14:51:21 | 107,969,414  |
| 2013-12 |              7089 |       6.46 | 2013-12-04 15:01:14 | 2014-01-16 06:59:35 | 107,608,630  |
| 2013-02 |              6477 |       5.90 | 2013-02-11 16:27:43 | 2013-03-05 12:16:15 | 170,625,168  |
| 2012-10 |              2922 |       2.67 | 2012-10-09 10:50:36 | 2012-10-29 11:03:21 | 40,077,499   |


# Map of Institutions

Every headquarter of a crawled institutions is mapped. Potential
branch offices are not depicted.


<div id="map" class="map"></div>
<div id="popup" class="ol-popup">
  <a href="#" id="popup-closer" class="ol-popup-closer"></a>
  <div id="popup-content"></div>
</div>


Coordinates provided by a crawl of Wikipedia on 2019-03-12.


<link rel="stylesheet"
href="https://cdn.rawgit.com/openlayers/openlayers.github.io/master/en/v5.3.0/css/ol.css"
type="text/css">

<style>
.map {
  height: 800px;
  width: 100%;
}
.ol-popup {
  position: absolute;
  background-color: white;
  -webkit-filter: drop-shadow(0 1px 4px rgba(0,0,0,0.2));
  filter: drop-shadow(0 1px 4px rgba(0,0,0,0.2));
  padding: 15px;
  border-radius: 10px;
  border: 1px solid #cccccc;
  bottom: 12px;
  left: -50px;
  min-width: 400px;
}
.ol-popup:after, .ol-popup:before {
  top: 100%;
  border: solid transparent;
  content: " ";
  height: 0;
  width: 0;
  position: absolute;
  pointer-events: none;
}
.ol-popup:after {
  border-top-color: white;
  border-width: 10px;
  left: 48px;
  margin-left: -10px;
}
.ol-popup:before {
  border-top-color: #cccccc;
  border-width: 11px;
  left: 48px;
  margin-left: -11px;
}
.ol-popup-closer {
  text-decoration: none;
  position: absolute;
  top: 2px;
  right: 8px;
}
.ol-popup-closer:after {
  content: "✖";
}
</style>

<script src="https://cdn.rawgit.com/openlayers/openlayers.github.io/master/en/v5.3.0/build/ol.js"></script>
<script type="text/javascript">
  /**
       * Elements that make up the popup.
       */
      var container = document.getElementById('popup');
      var content = document.getElementById('popup-content');
      var closer = document.getElementById('popup-closer');

      /**
       * Create an overlay to anchor the popup to the map.
       */
      var overlay = new ol.Overlay({
        element: container,
        autoPan: true,
        autoPanAnimation: {
          duration: 250
        }
      });

      /**
       * Add a click handler to hide the popup.
       * @return {boolean} Don't follow the href.
       */
      closer.onclick = function() {
        overlay.setPosition(undefined);
        closer.blur();
        return false;
      };

      /**
       * Get data for markers and popups
       */
      var vectorSource = new ol.source.Vector({
        url: 'assets/geodata.geojson',
        format: new ol.format.GeoJSON(),
      });

      /**
       * Create the map.
       */
      var map = new ol.Map({
        target: 'map',
        layers: [
          new ol.layer.Tile({
            source: new ol.source.OSM()
          }),
          new ol.layer.Vector({
            source: vectorSource,
            style: new ol.style.Style({
              image: new ol.style.Circle({
                radius: 4,
                fill: new ol.style.Fill({color: 'blue'})
              })
            })
          })
        ],
        overlays: [overlay],
        view: new ol.View({
          center: ol.proj.fromLonLat([10.018343, 51.133481]),
          zoom: 6
        })
      });

      /**
       * Get the aggregated data.
       */
      var displayFeatureInfo = function(pixel) {
        var features = [];
        map.forEachFeatureAtPixel(pixel, function(feature, layer) {
          features.push(feature);
        });
        if (features.length > 0) {
          var showing = [];
          for (var i = 0, ii = features.length; i < ii; ++i) {
            showing.push('<a target="_blank" href="' + (features[i].get('Subsite')) + '">' + (features[i].get('Name')) + '</a>');
          }
          if (showing.length > 1) {
            content.innerHTML = showing.join('<br>') || '(unknown)';
          }
          else if (showing.length == 1) {
            content.innerHTML = showing;
          }
        } else {
          content.innerHTML = 'No institution selected';
        }
      };

      /**
       * Add a click handler to the map to render the popup.
       */
      map.on('click', function(evt) {
        var pixel = evt.pixel;
        displayFeatureInfo(pixel);
        overlay.setPosition(evt.coordinate);
      });
</script>
