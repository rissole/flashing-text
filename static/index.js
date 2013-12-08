//literally Adobe/Macromedia/Shockwave flash DAE 90s?
ZeroClipboard.setDefaults({
    moviePath: "http://cdnjs.cloudflare.com/ajax/libs/zeroclipboard/1.2.3/ZeroClipboard.swf",
    trustedOrigins: [window.location.protocol + "//" + window.location.host]
});
function basedURL(uriEncodeInput) {
    if (typeof uriEncodeInput === 'undefined') {
        encoded = true;
    }
    //programming
    var theGoods = $('#uwotm8').val();
    if (uriEncodeInput) {
        theGoods = encodeURIComponent(theGoods);
    }
    if ($('#encrypted').is(':checked')) {
        theGoods = window.btoa(theGoods);
        theGoods = 'e/'+theGoods;
    }
    return window.location.protocol + '//' + window.location.host + '/' + theGoods;
}

function updateLinkShares() {
    $('#link-shares > a.link-fb').attr('href', 'https://facebook.com/sharer/sharer.php?u='+encodeURIComponent(basedURL(false)));
    $('#link-shares > a.link-tw').attr('href', 'https://twitter.com/share?url='+encodeURIComponent(basedURL(false)));
}

var goToBasedURL = function() {
    document.location.href = basedURL();
};

$('#uwotm8').on('input', function() {
    $('#output').val(basedURL());
    updateLinkShares();
});

$('#nike').click(function() {
    goToBasedURL();
});

$('.basedform').submit(function(e) {
    goToBasedURL();
    return false; // returning false prevents the form from submitting suuuuuuuuuuuuuuuuuuuuuuuuuuuure js
});

$('input[name=linktype]').change(function() { $('#uwotm8').trigger('input') });

$('a[data-popup]').click(function() {
    window.open(this.href, 'Share', 'width=400,height=300,toolbar=no,menubar=no,scrollbars=no,location=no,directories=no');
    return false;
});

$('div.input-group').tooltip({
    'placement': 'right',
    'title': 'Copied!',
    'trigger': 'manual'
});

var clip = new ZeroClipboard($('#copy-button'));
clip.on('load', function(client) {
    client.on('complete', function(client, args) {
        $('div.input-group').tooltip('show');
    });
});
