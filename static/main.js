function encodeHtml(s) {
    return s.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/"/g, '&quot;');
}

function getBotResponse() {
    const rawText = document.getElementById("msg-box").value;
    const userMsg = '<p class="user-msg">' + encodeHtml(rawText) + '</p>';
    document.getElementById("msg-box").value = "";
    document.getElementById("chatbox").append(userMsg);
    document.getElementById("msg-box").scrollIntoView({ block: "start", behavior: "smooth" });

    let xhr = new XMLHttpRequest();
    xhr.open("POST", "/get", false);
    xhr.send({ msg: rawText });

    const botText = xhr.responseText;
    if (!special(botText)) {
        const botMsg = '<p class="bot-msg">' + botText + '</p>';
        document.getElementById("chatbox").append(botMsg);
    } else {
        const newText = doStuff(botText);
        const botMsg = '<p class="bot-msg">' + newText + '</p>';
        document.getElementById("chatbox").append(botMsg);
    }
}

function special(s) {
    return s.search(/^OPEN BROWSER/) !== -1;
}

function doStuff(s) {
    const url = s.replace("OPEN BROWSER: ", "").replace("##", "")
    browser.open(url);
}

document.getElementById('msg-box').addEventListener('keypress', event => {
    if (event.which === 13) {
        getBotResponse();
    }
});