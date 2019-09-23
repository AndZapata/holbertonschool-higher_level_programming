#!/usr/bin/node
exports.converter = function (base) {
  return function (numObj) {
    return (numObj.toString(base));
  };
};
