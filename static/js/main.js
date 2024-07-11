function showMore() {
    var pageCur = Number(document.getElementById("page-cur").value);
    var pageNum = Number(document.getElementById("page-num").value);
  
    pageCur += 1
    fetch('?page=' + pageCur, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
        .then(response => {
            console.log(response)
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.text()
        })
        .then(data => {
            document.getElementsByClassName("poll-container")[0].innerHTML += data;
            document.getElementById("page-cur").value = pageCur;

            if(pageCur == pageNum){
                document.getElementById("show-more").classList.add("disabled");
            }

            var numPages = document.getElementsByClassName("pagination")[0];
            let ind = 1
            for (let nP of numPages.children) {
                
                nP.classList.remove("active");
                nP.classList.remove("disabled");
                
                if(pageCur == ind) {
                    nP.classList.add("disabled");
                }
                ind ++;
            }
        })
        .catch(error => console.log('Error:', error));
}

document.getElementById('searchInput').addEventListener('input', function () {
    var query = this.value;

    fetch(`?q=${query}`, {
        headers: {
            'X-Requested-With': 'XMLHttpRequest'
        }
    })
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not ok ' + response.statusText);
            }
            return response.text();
        })
        .then(data => {
            document.getElementsByClassName('poll-container')[0].innerHTML = data;
        })
        .catch(error => console.error('Error:', error));
});

