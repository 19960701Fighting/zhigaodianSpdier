// encryptKey = 'Xa2dbtJvt9DuvaNl';

function stringToCharArray(value) {
    var cs = [];
    for (var i = 0; i < value.length; i++) {
        cs[i] = value.charAt(i)
    }
    return cs
}

function charArrayToString(cs) {
    var result = "";
    for (var i = 0; i < cs.length; i++) {
        result += cs[i]
    }
    return result
}

function encrypt(value, key) {
    var cs = stringToCharArray(value);
    for (var i = 0; i < cs.length; i++) {
        var t = cs[i];
        var newIdex = key.charCodeAt(i % key.length) % cs.length;
        cs[i] = cs[newIdex];
        cs[newIdex] = t
    }
    return charArrayToString(cs)
}

function decrypt(value, key) {
    var cs = value.toCharArray();
    for (var i = cs.length - 1; i >= 0; i--) {
        var t = cs[i];
        var newIdex = key.charCodeAt(i % key.length) % cs.length;
        cs[i] = cs[newIdex];
        cs[newIdex] = t
    }
    return charArrayToString(cs)
}

function appendToken(href, resourceToken, encryptKey) {
    var startIndex = href.lastIndexOf('/');
    var endIndex = href.indexOf('.');
    if (endIndex < startIndex) {
        endIndex = href.length
    }
    var name = href.substring(startIndex + 1, endIndex);
    var token = encrypt(resourceToken, name + encryptKey);
    href += "?token=" + token;
    return href
}

function bindTokens() {
    $(".token-autowired").each(function () {
        var attrName = "href";
        if ($(this).is('img')) {
            attrName = "src"
        }
        var href = $(this).attr(attrName);
        $(this).attr(attrName, appendToken(href))
    })
}

// $(document).ready(bindTokens);
// $(document).bind("reReady", bindTokens);