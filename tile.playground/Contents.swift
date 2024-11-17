//: Playground - noun: a place where people can play

import UIKit

var str = "Hello, playground"

let textField = UITextField(frame: CGRect(x: 0, y: 0, width: 200, height: 100))
textField.borderStyle = .RoundedRect
textField.text = "200"
textField.sizeToFit()
let textField2 = UITextField(frame: CGRect(x: 0, y: 0, width: 200, height: 100))
textField2.borderStyle = .RoundedRect
textField2.text = "300"
textField2.sizeToFit()
var height = 0 // Just some random values
var width = 1 // These don't actually matter right now

height = textField.text.toInt()!
width = textField2.text.toInt()!

//var height = 8
//var width = 9

var area = (width * height)

//ar total = area * 1.1


