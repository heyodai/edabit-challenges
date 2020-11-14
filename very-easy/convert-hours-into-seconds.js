/**
 * Nov 13, 2020
 * https://edabit.com/challenge/6AnQqiEjkJdZrWhPS
 */


/**
 * Take a quantity of hours and output the equivalent in seconds
 * @param {int} hours The number of hours to convert
 * @returns {int} The number of seconds 
 */
function howManySeconds(hours) {
    const MULTIPLIER = 60; // seconds in a minute, minutes in an hour
    var minutes = hours * MULTIPLIER;
    var seconds = minutes * MULTIPLIER;
    return seconds;
}