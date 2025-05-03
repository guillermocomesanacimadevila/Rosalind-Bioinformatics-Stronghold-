const fs = require('fs');
const path = require('path');

function fastaAnalysis() {
    const filePath = path.resolve('/Users/guillermocomesanacimadevila/Desktop/HFE_datasets/ncbi_dataset/data/gene.fna');
    const fasta = fs.readFileSync(filePath, 'utf-8');
    const lines = fasta.split('\n');

    const counter = { A: 0, T: 0, C: 0, G: 0 };
    const sequences = {};
    let currentHeader = null;
    let currentSequence = [];

    for (let line of lines) {
        line = line.trim();
        if (line.startsWith('>')) {
            if (currentHeader) {
                sequences[currentHeader] = currentSequence.join('');
            }
            currentHeader = line.slice(1);
            currentSequence = [];
        } else {
            currentSequence.push(line);
            for (let nuc of line) {
                if (counter.hasOwnProperty(nuc)) {
                    counter[nuc]++;
                }
            }
        }
    }

    if (currentHeader) {
        sequences[currentHeader] = currentSequence.join('');
    }

    const totalBases = Object.values(counter).reduce((a, b) => a + b, 0);
    const gcCount = counter.G + counter.C;
    const gcContent = totalBases > 0 ? (gcCount / totalBases) * 100 : 0;

    const sequenceValues = Object.values(sequences);
    console.log("Number of sequences:", sequenceValues.length);
    console.log("GC Content:", gcContent.toFixed(2) + "%");
    console.log("Nucleotide counts:", counter);

    // Longest and shortest sequences
    const lengthMap = Object.entries(sequences).map(([header, seq]) => ({
        header,
        length: seq.length
    }));

    const longest = lengthMap.reduce((a, b) => (b.length > a.length ? b : a));
    const shortest = lengthMap.reduce((a, b) => (b.length < a.length ? b : a));

    console.log("Longest:", longest.header.slice(0, 5), "Length:", longest.length);
    console.log("Shortest:", shortest.header.slice(0, 5), "Length:", shortest.length);

    // Reverse complement (just reverse, not complement)
    const allSeq = sequenceValues.join('');
    const revComp = allSeq.split('').reverse().join('');
    console.log("Reverse sequence preview:", revComp.slice(0, 60) + "...");

    // Find motif
    const motif = "ATG";
    const motifPositions = [];
    for (let i = 0; i <= allSeq.length - motif.length; i++) {
        if (allSeq.slice(i, i + motif.length) === motif) {
            motifPositions.push(i);
        }
    }
    console.log(`Motif '${motif}' found at positions:`, motifPositions);

    return { sequenceValues, gcContent, counter };
}

fastaAnalysis();
