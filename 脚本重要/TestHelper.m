//
//  TestHelper.m
//  jiasuqi
//
//  Created by shenghuihan on 16/10/13.
//  Copyright © 2016年 shenghuihan. All rights reserved.
//

#import "TestHelper.h"
#import "ASIHTTPRequest.h"

@interface TestHelper()
@property (nonatomic, copy) void(^completeBlcok)(NSDictionary *);
@property (nonatomic, copy) void(^errorBlcok)(NSError *);
@end

@implementation TestHelper

static id _helper;

+ (instancetype)allocWithZone:(struct _NSZone *)zone {
    static dispatch_once_t onceToken;
    dispatch_once(&onceToken, ^{
        _helper = [super allocWithZone:zone];
    });
    
    return _helper;
}

+ (instancetype)shareCar {
    //init方法即使反复调用，只要是针对同一份内存，也不会修改其属性的值，所以这里不需要设置一次性执行，当然你如果说为了效率也是可以的，不过无所谓这里
    _helper = [[TestHelper alloc] init];
    return _helper;
}

- (id)copyWithZone:(NSZone *)zone {
    return _helper;
}

- (id)mutableCopyWithZone:(NSZone *)zone {
    return _helper;
}

+ (NSDictionary *)getData:(NSString *)fileName {
    
    NSArray *paths = NSSearchPathForDirectoriesInDomains (NSDocumentDirectory, NSUserDomainMask, YES);
    NSString *localPath = [paths objectAtIndex:0];
    
    NSArray *pathsArr = [localPath componentsSeparatedByString:@"/"];
    NSString *deskTopPath;
    
    if (pathsArr.count <= 3) return nil;
    
    deskTopPath = [NSString stringWithFormat:@"/%@/%@/Desktop", pathsArr[1], pathsArr[2]];
    
    
    NSString* thepath = deskTopPath;
    thepath = [thepath stringByAppendingPathComponent:fileName];
    NSData *data = [NSData dataWithContentsOfFile:thepath];
    
    if (!data) {
        NSLog(@"data为空");
        return nil;
    }
    
    return [self handleData:data];
}

+ (NSDictionary *)getDataFromBundleWithName:(NSString *)name type:(NSString *)typeString {
    
    NSString *thepath = [[NSBundle mainBundle] pathForResource:name ofType:typeString];
    
    NSData *data = [NSData dataWithContentsOfFile:thepath];
    
    if (!data) {
        NSLog(@"data为空");
        return nil;
    }
    
    return [self handleData:data];
}

+ (NSDictionary *)handleData:(NSData *)data {
    
    NSError *error = nil;
    
    NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:data options:NSJSONReadingMutableLeaves error:&error];

    NSLog(@"字典%@", dic);
    
    if (error) {
        NSLog(@"%@", error);
        return nil;
    }
    
    return dic;
}

/* 用法
 TestHelper *helper = [[TestHelper alloc] init];
 [helper requesDataWithHost:@"http://10.13.79.25:89/" AndUrl:@"url1" AndCompleteBlock:^(NSDictionary *dic) {
 NSLog(@"%@", dic);
 } AndErrorBlock:^(NSError *error) {
 NSLog(@"%@", error);
 }];
 */

- (void)requesDataWithHost:(NSString *)host AndUrl:(NSString *)url AndCompleteBlock:(void(^)(NSDictionary *))completeBlock AndErrorBlock:(void(^)(NSError *))errorBlock {
    self.completeBlcok = completeBlock;
    self.errorBlcok = errorBlock;
    
    NSString *urlString = [NSString stringWithFormat:@"%@%@", host, url];
    NSURL *resultUrl = [NSURL URLWithString:urlString];
    ASIHTTPRequest *request = [ASIHTTPRequest requestWithURL:resultUrl];
    [request setDelegate:self];
    [request startAsynchronous];
}

- (void)requestFinished:(ASIHTTPRequest *)request
{
    // Use when fetching text data
    NSString *responseString = [request responseString];
    // Use when fetching binary data
//    NSData *responseData = [request responseData];
    NSLog(@"---->%@",responseString);
    
    NSData *responseData = [responseString dataUsingEncoding:NSUTF8StringEncoding];
    NSError *error = nil;
    NSDictionary *dic = [NSJSONSerialization JSONObjectWithData:responseData options:NSJSONReadingMutableLeaves error:&error];
    
    if (self.completeBlcok) {
        self.completeBlcok(dic);
    }
}

- (void)requestFailed:(ASIHTTPRequest *)request
{
    NSError *error = [request error];
    NSLog(@"error%@", error);
    if (self.errorBlcok) {
        self.errorBlcok(error);
    }
}

@end
