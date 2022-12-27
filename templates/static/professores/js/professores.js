function exibir_form(tipo) {
  const addProf = document.getElementById('addProf');
  const attProf = document.getElementById('attProf');

  if (tipo == 1) {
    attProf.style.display = 'none';
    addProf.style.display = 'block';
  } else if (tipo == 2) {
    addProf.style.display = 'none';
    attProf.style.display = 'block';
  }
}

function dadosProf() {
  const professor = document.getElementById('selectProf');
  const csrf_token = document.querySelector('[name=csrfmiddlewaretoken]')
  const idProf = professor.value
  const data = new FormData()
  data.append('idProf',idProf )
  fetch("/professores/attProfessor/",{
    method: "POST",
    headers: {
      'X-CSRFToken': csrf_token,
    },
    body:
  })
}
