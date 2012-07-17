// jquery for pystar


$(document).ready(function(){
    // twitter mentions
    $('#twitter-area').twitterMentions(['#pystar', '#pystarmpls', 'pystar.org', 'pystarphilly', '@PyStarPhilly'],{ 
                avatar : true,
                maximum : 6,
                ulClass : 'twitter-mentions',
                odd : true,
                oddClass : 'odd'
        }
    );

    // button bar
    
    var buttonbar;
    buttonbar=$("<span class='button-bar'>" +
        "<div class='expand-zoom-1 toggle-zoom-1'>show more</div>" +
        "<div class='collapse-zoom-1 toggle-zoom-1'>show less</div>" +
        "<span>").css(
        {bottom: 0, right:0, 
         border:'2px dashed red', 
         backgroundColor: 'white',
         margin: '10px', 
         position: 'fixed' }
    
    );

    // $('body').append(buttonbar);

    // expand collapse zoom levels.  needs refactor!
    $('.zoom-1').before(
        "<div class='expand-zoom-1 toggle-zoom-1'>[ show more ]</div>" +
        "<div class='collapse-zoom-1 toggle-zoom-1'>[ show less ]</div>"
        ); 
    $('.zoom-1').css('border','10px red solid').hide();
    $('.collapse-zoom-1').hide();
    $('.expand-zoom-1').show();

    $('.toggle-zoom-1').click(function(){
        $('.zoom-1').toggle();
        $('.collapse-zoom-1').toggle();
        $('.expand-zoom-1').toggle();
    });

    // ? help on glossary terms
     $('a[href^="#term"]').after("<span title='this would be the glossary item text.'> [?] </span>");
    /*
    // this doesn't work!
    $('a[href^="#term"]').after(function(){
        var href=$(this).attr('href');
        var term='environment';
        return ($.get($(this).attr('href')), function(data) {
            return ($('dt.term-environment').html()) ;
        }))
    });*/



    // make it sortable!  Whoa!
    $(".sortable").tablesorter();

    // 
});


// social button
$(function() {

    $('.socialbutton:after').css({
	    'content': ".",
	    'display': 'block',
	    'height': 0,
	    'clear': 'both',
	    'visibility': 'hidden'
    });
    
    $('.socialbutton').css(
	    {'display': 'inline-block'});

    $('.socialbutton div').css({
	    'margin-right': '15px',
	    'float': 'left',
    });

    $('#evernote2').socialbutton('evernote', {
        button: 'site-mem-22',
        styling: 'full'
    });

    $('#hatena2').socialbutton('hatena', {
        button: 'simple'
    });

    $('#mixi2').socialbutton('mixi_check', {
        button: 'button-1',
        key: '3acaac24ec3181bf5d27bfdd86c5a5b7a108d04c'
    });

    $('#gree2').socialbutton('gree_sf', {
        button: 4,
        height: 22
    });

    $('#twitter2').socialbutton('twitter', {
        button: 'none',
        text: 'some twitter tweet ',
        via: 'some_twitter_user'
    });

    $('#facebook_like2').socialbutton('facebook_like', {
        button: 'button_count'
    });

    $('#facebook_share2').socialbutton('facebook_share', {
        button: 'button',
        text: 'share it'
    });

});


// add accordian style answers
$(function(){
    $('.answer-hidden').prepend('<span class="answerheader">Answer (click)</span>');
    $('.answer-hidden').accordion({collapsible: true,active: false,header: 'span.answerheader'});
})

