const sol = (str) => {
    let result = ''

    for(let s of str) {
        result += s.toUpperCase()
    }
    return result
}

console.log(sol('ItisTimeToStudy'))