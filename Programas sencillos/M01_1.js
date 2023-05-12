// # Anagramas
// # Crear un programa que indique si una cadena es un anagrama de otra (mismos carácteres en orden diferente). Ejemplo

// # Primera cadena: otra
// # Segunda cadena: rota

// # "otra" y "rota" son anagramas
// # Restricciones
// # Hacerlo con la función esAnagrama
// # Ambas palabras deben tener la misma longitud
// # Reto
// # Hacerlo sin las facilidades de manejo de cadenas de python

function is_anagram(word1, word2) {
  if (word1.length !== word2.length) {
    console.log('False');
    return false;
  }

  let listword2 = word2.split('');

  for (let letter of word1) {
    console.log(listword2);
    for (let i = 0; i < word2.length; i++) {
      if (letter === listword2[i]) {
        listword2[i] = '*';
        break;
      }
    }
  }

  console.log(listword2);
  const comp = '*'.repeat(word2.length);
  word2 = listword2.join('');
  console.log(`${comp} vs ${word2}`);
  console.log('True');
  return comp === word2;
}


function is_anagram2(word1, word2) {
  if (word1.length !== word2.length) {
    console.log('False');
    return false;
  }

  let position = [];

  for (let i = 0; i < word1.length; i++) {
    console.log(position);
    for (let j = 0; j < word2.length; j++) {
      if (word1[i] === word2[j] && !position.includes(j)) {
        position.push(j);
        break;
      }
    }
  }

  console.log(position);
  console.log('True');
  return position.length === word2.length;
}

is_anagram('otra', 'arto');
is_anagram2('reto', 'oer');
