//
//  ViewController.h
//  MyApp
//
//  Created by LinhND on 6/18/18.
//  Copyright © 2018 LinhND. All rights reserved.
//

#import <UIKit/UIKit.h>

@interface ViewController : UIViewController

@property (weak, nonatomic) IBOutlet UILabel *label;
@property (weak, nonatomic) IBOutlet UITextField *textField;
@property (weak, nonatomic) IBOutlet UIButton *button;

- (IBAction)buttonPressed:(id)sender;
@end

