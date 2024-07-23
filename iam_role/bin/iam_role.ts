#!/usr/bin/env node
import * as cdk from 'aws-cdk-lib';
import { IamRoleStack } from '../lib/iam_role-stack';

const app = new cdk.App();
new IamRoleStack(app, 'IamRoleStack');
