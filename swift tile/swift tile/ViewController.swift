//
//  ViewController.swift
//  swift tile
//
//  Created by preston hawkes on 5/16/15.
//  Copyright (c) 2015 preston hawkes. All rights reserved.
//

import UIKit

class ViewController: UIViewController {

    @IBOutlet weak var widthtextfield: UITextField!
    
    @IBOutlet weak var heighttextfield: UITextField!
    
    @IBOutlet weak var costpertiletextfield: UITextField!
    
    @IBOutlet weak var costbitchestextfield: UITextField!
    
    override func viewDidLoad() {
        super.viewDidLoad()
        // Do any additional setup after loading the view, typically from a nib.
        var timer=NSTimer.scheduledTimerWithTimeInterval(0.5, target: self, selector: Selector("CalcCostBitches"), userInfo: nil, repeats: true)
    }

    override func didReceiveMemoryWarning() {
        super.didReceiveMemoryWarning()
        // Dispose of any resources that can be recreated.
    }

    func CalcCostBitches() {
        var width:Int
        var height:Int
        var costpertile:Int
        var costbitches:Double
        
        width = widthtextfield.text.toInt()!
        height = heighttextfield.text.toInt()!
        costpertile = costpertiletextfield.text.toInt()!
        
        costbitches = Double(width) * Double(height) * Double(costpertile) * 1.1
        
        costbitchestextfield.text = String(format: "%f", costbitches)
    }

}

