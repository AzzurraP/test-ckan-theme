"use strict";

ckan.module('feedreader', function ($, _) {
  return {
   options: {
      url: ''
    },
    initialize: function () {
	
	
	var self=this;
		 //$(this.el).FeedEk({
		//	FeedUrl: this.options.url
		//});
		
		$(this.el).rss(this.options.url,{
    limit: 3,
    key: 'm5fatrddtmqwabbbultqef2hzom2apya7cl8ymbc',
    layoutTemplate: '<div id="owl-carousel" class="owl-carousel">{entries}</div>',
    //entryTemplate: ' <div><h3><a href="{url}" target="_blank">{title}</a></h3><div>{teaserImage}</div><br/><p>{shortBodyPlain}</p> </div>'
    entryTemplate: ' <div><h3><a href="{url}" target="_blank">{title}</a></h3><br/><p>{shortBodyPlain}</p> </div>'
	,
	success: function(){

	  $('#' + self.options.owlid).owlCarousel({
	 
		  navigation : false, // Show next and prev buttons
		  slideSpeed : 1000,
		  paginationSpeed : 400,
		  singleItem:true,
		  autoPlay: true,
		   mouseDrag:false
	  });
	 

	}
});
		
		
		
    }
  };
});
