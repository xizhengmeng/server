//
//  TestHelper.h
//  jiasuqi
//
//  Created by shenghuihan on 16/10/13.
//  Copyright © 2016年 shenghuihan. All rights reserved.
//

#import <Foundation/Foundation.h>

@interface TestHelper : NSObject
+ (NSDictionary *)getData:(NSString *)url;
+ (NSDictionary *)getDataFromBundleWithName:(NSString *)name type:(NSString *)typeString;
- (void)requesDataWithHost:(NSString *)host AndUrl:(NSString *)url AndCompleteBlock:(void(^)(NSDictionary *))completeBlock AndErrorBlock:(void(^)(NSError *))errorBlock;
@end
