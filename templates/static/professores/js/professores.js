function exibir_form(tipo) {
  addProf = document.getElementById('addProf');
  attProf = document.getElementById('attProf');

  if (tipo == 1) {
    attProf.style.display = 'none';
    addProf.style.display = 'block';
  } else if (tipo == 2) {
    addProf.style.display = 'none';
    attProf.style.display = 'block';
  }
}
