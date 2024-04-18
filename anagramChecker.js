console.log("This is an angrams checker");
console.log("It checks that the length is the same and all the letters in both words are the same");

function anagramChecker (firstWord, secondWord) {

    var word_1 = [...firstWord].sort();
    var word_2 = [...secondWord].sort();

    var word1_length = firstWord.length;
    var word2_length = secondWord.length;

    if (word1_length == word2_length){

        if (word_1.join() == word_2.join()) {
            console.log("Anagrams");
        }
        else{
            console.log("Ooops...Same length not anagrams");
        };
    }
    else{
        console.log("Not anagrams");
    };
};

var word1 = prompt("Enter the first word");
var word2 = prompt("Enter the second word");

anagramChecker(word1, word2);

