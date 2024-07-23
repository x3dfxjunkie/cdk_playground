import { Stack, StackProps } from 'aws-cdk-lib';
import * as aws_iam from 'aws-cdk-lib/aws-iam';
import { Construct } from 'constructs';

export class IamRoleStack extends Stack {
  constructor(scope: Construct, id: string, props?: StackProps) {
    super(scope, id, props);

    const codebuildRole = new aws_iam.Role(this, 'CodebuildRole', {
      assumedBy: new aws_iam.ServicePrincipal('codebuild.amazonaws.com'),
    });

    codebuildRole.addToPolicy(new aws_iam.PolicyStatement({
      actions: [
        '*'
    ],
      resources: [ '*' ],
    }));

  }
}
