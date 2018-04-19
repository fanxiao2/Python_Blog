(function($){

  /* External links */
  $(document).ready(function() {
    $('a[href]').each(function() {
      if (this.href.indexOf(window.location.host) == -1) $(this).attr({target: '_blank' });
    });

    var handler=function(hash){
      var target = document.getElementById(hash.slice(1));
      if (!target) return;
      var targetOffset = $(target).offset().top-70;
      $('html,body').animate({scrollTop: targetOffset}, 400);
    }

    $('a[href^=#][href!=#]').click(function(){
      handler(this.hash)
    });
    if(location.hash){ handler(location.hash) }
  });

  /* site search */
  $(document).ready(function() {
    var entries = null;
    function htmlEscape(s) {
      return String(s).replace(/[&<>"'\/]/g, function(s) {
        var entityMap = {
          "&": "&amp;",
             "<": "&lt;",
             ">": "&gt;",
             '"': '&quot;',
             "'": '&#39;',
             "/": '&#x2F;'
        };
        return entityMap[s];
        });
    }
    function xmlDateToJavascriptDate(xmlDate) {
      var re = /^([0-9]{4,})-([0-9]{2})-([0-9]{2})T([0-9]{2}):([0-9]{2}):([0-9]{2})(\.[0-9]+)?(Z|([+-])([0-9]{2}):([0-9]{2}))?$/;
      var match = xmlDate.match(re);
      if (!match)
        return null;
      var all = match[0];
      var year = match[1];  var month = match[2];  var day = match[3];
      var hour = match[4];  var minute = match[5]; var second = match[6];
      var milli = match[7];
      var z_or_offset = match[8];  var offset_sign = match[9];
      var offset_hour = match[10]; var offset_minute = match[11];
      if (offset_sign) {
        var direction = (offset_sign == "+" ? 1 : -1);
        hour =   parseInt(hour)   + parseInt(offset_hour)   * direction;
        minute = parseInt(minute) + parseInt(offset_minute) * direction;
      }
      month = parseInt(month) - 1;
      var utcDate = Date.UTC(year, month, day, hour, minute, second, (milli || 0));
      return new Date(utcDate);
    }
    function formatDate(date) {
      return date.getFullYear()+"-"+ (date.getMonth()+1)+ '-' + date.getDate();
    }
    function findEntries(q) {
      var matches = [];
      var rq = new RegExp(q, 'im');
      var rl = /^http:\/\/blog\.javachen\.com\/(.+)$/;
      for (var i = 0; i < entries.length; i++) {
        var entry = entries[i];
        var title = $(entry.getElementsByTagName('title')[0]).text();
        var link = $(entry.getElementsByTagName('link')[0]).text();
        var description = $(entry.getElementsByTagName('description')[0]).text();
        if (rq.test(title) || rq.test(description)) {
          var pubDate = formatDate(xmlDateToJavascriptDate($(entry.getElementsByTagName('pubDate')[0]).text()));
          matches.push({'title': title, 'link': link, 'pubDate': pubDate, 'description': description});
        }
      }
      var html = '<h3>Search Result:</h3>';
      for (var i = 0; i < matches.length; i++) {
        var match = matches[i];
        html += ' <div id="home-post"><h4><a href="' + match.link + '" target="_blank">' + htmlEscape(match.title) + '</a>&nbsp;<small>'+match.pubDate+'</small></h4>';
        //html += '<div id="home-post-text">' + match.description + '</div>';
        html+="</div>"
      }
      $('#wrap .container').html(html);
      $('#wrap .container').show();
    }

    $('#search-form').submit(function() {
      var query = $('#query').val();
      $('#wrap .container').hide();
      if (!entries) {
        $.ajax({url: '/rss.xml?r=' + (Math.random() * 99999999999), dataType: 'xml', success: function(data) {
          entries = data.getElementsByTagName('item');
          findEntries(query);
        }});
      } else {
        findEntries(query);
      }
      $('#query').blur().attr('disabled', false);
      return false;
    });

    });

  })(jQuery);
