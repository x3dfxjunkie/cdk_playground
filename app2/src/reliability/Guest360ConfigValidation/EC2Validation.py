import aws_cdk.aws_ec2 as ec2
import logging
from typing import Union

logger = logging.getLogger()
logger.setLevel(logging.INFO)

class Guest360ConfigEC2Validation():
    """EC2 validation methods that are used to ensure configuration values are checked against valid types.
    """

    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/InstanceClass.html
    # Full List provisioned on 2022_09_19
    def getEC2ReplicationInstanceClass(instance_class: str) ->  Union[ec2.InstanceClass, None]:
        """Returns Literal ec2.InstanceClass.<instance_class> if a valid instance_class is passed in
        https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/InstanceClass.html
        
        Args:
            instance_class (str): Instance class of the machine (i.e. A1, BURSTABLE3, M4, M5)

        Returns:
            ec2.InstanceClass | None: returns literal value for the instance_class. i.e. ec2.InstanceClass.BURSTABLE3
        """
        if instance_class == "A1":
            return ec2.InstanceClass.A1
        elif instance_class == "ARM1":
            return ec2.InstanceClass.ARM1
        elif instance_class == "BURSTABLE2":
            return ec2.InstanceClass.BURSTABLE2
        elif instance_class == "BURSTABLE3":
            return ec2.InstanceClass.BURSTABLE3
        elif instance_class == "BURSTABLE3_AMD":
            return ec2.InstanceClass.BURSTABLE3_AMD
        elif instance_class == "BURSTABLE4_GRAVITON":
            return ec2.InstanceClass.BURSTABLE4_GRAVITON
        elif instance_class == "C3":
            return ec2.InstanceClass.C3
        elif instance_class == "C4":
            return ec2.InstanceClass.C4
        elif instance_class == "C5":
            return ec2.InstanceClass.C5
        elif instance_class == "C5A":
            return ec2.InstanceClass.C5A
        elif instance_class == "C5AD":
            return ec2.InstanceClass.C5AD
        elif instance_class == "C5D":
            return ec2.InstanceClass.C5D
        elif instance_class == "C5N":
            return ec2.InstanceClass.C5N
        elif instance_class == "C6A":
            return ec2.InstanceClass.C6A
        elif instance_class == "C6G":
            return ec2.InstanceClass.C6G
        elif instance_class == "C6GD":
            return ec2.InstanceClass.C6GD
        elif instance_class == "C6GN":
            return ec2.InstanceClass.C6GN
        elif instance_class == "C6I":
            return ec2.InstanceClass.C6I
        elif instance_class == "C6ID":
            return ec2.InstanceClass.C6ID
        elif instance_class == "C7G":
            return ec2.InstanceClass.C7G
        elif instance_class == "COMPUTE3":
            return ec2.InstanceClass.COMPUTE3
        elif instance_class == "COMPUTE4":
            return ec2.InstanceClass.COMPUTE4
        elif instance_class == "COMPUTE5":
            return ec2.InstanceClass.COMPUTE5
        elif instance_class == "COMPUTE5_AMD":
            return ec2.InstanceClass.COMPUTE5_AMD
        elif instance_class == "COMPUTE5_AMD_NVME_DRIVE":
            return ec2.InstanceClass.COMPUTE5_AMD_NVME_DRIVE
        elif instance_class == "COMPUTE5_HIGH_PERFORMANCE":
            return ec2.InstanceClass.COMPUTE5_HIGH_PERFORMANCE
        elif instance_class == "COMPUTE5_NVME_DRIVE":
            return ec2.InstanceClass.COMPUTE5_NVME_DRIVE
        elif instance_class == "COMPUTE6_AMD":
            return ec2.InstanceClass.COMPUTE6_AMD
        elif instance_class == "COMPUTE6_GRAVITON2":
            return ec2.InstanceClass.COMPUTE6_GRAVITON2
        elif instance_class == "COMPUTE6_GRAVITON2_HIGH_NETWORK_BANDWIDTH":
            return ec2.InstanceClass.COMPUTE6_GRAVITON2_HIGH_NETWORK_BANDWIDTH
        elif instance_class == "COMPUTE6_GRAVITON2_HIGH_NETWORK_BANDWITH":
            return ec2.InstanceClass.COMPUTE6_GRAVITON2_HIGH_NETWORK_BANDWITH
        elif instance_class == "COMPUTE6_GRAVITON2_NVME_DRIVE":
            return ec2.InstanceClass.COMPUTE6_GRAVITON2_NVME_DRIVE
        elif instance_class == "COMPUTE6_INTEL":
            return ec2.InstanceClass.COMPUTE6_INTEL
        elif instance_class == "COMPUTE6_INTEL_NVME_DRIVE":
            return ec2.InstanceClass.COMPUTE6_INTEL_NVME_DRIVE
        elif instance_class == "COMPUTE7_GRAVITON3":
            return ec2.InstanceClass.COMPUTE7_GRAVITON3
        elif instance_class == "D2":
            return ec2.InstanceClass.D2
        elif instance_class == "D3":
            return ec2.InstanceClass.D3
        elif instance_class == "D3EN":
            return ec2.InstanceClass.D3EN
        elif instance_class == "DEEP_LEARNING1":
            return ec2.InstanceClass.DEEP_LEARNING1
        elif instance_class == "DL1":
            return ec2.InstanceClass.DL1
        elif instance_class == "F1":
            return ec2.InstanceClass.F1
        elif instance_class == "FPGA1":
            return ec2.InstanceClass.FPGA1
        elif instance_class == "G3":
            return ec2.InstanceClass.G3
        elif instance_class == "G3S":
            return ec2.InstanceClass.G3S
        elif instance_class == "G4AD":
            return ec2.InstanceClass.G4AD
        elif instance_class == "G4DN":
            return ec2.InstanceClass.G4DN
        elif instance_class == "G5":
            return ec2.InstanceClass.G5
        elif instance_class == "G5G":
            return ec2.InstanceClass.G5G
        elif instance_class == "GRAPHICS3":
            return ec2.InstanceClass.GRAPHICS3
        elif instance_class == "GRAPHICS3_SMALL":
            return ec2.InstanceClass.GRAPHICS3_SMALL
        elif instance_class == "GRAPHICS4_AMD_NVME_DRIVE":
            return ec2.InstanceClass.GRAPHICS4_AMD_NVME_DRIVE
        elif instance_class == "GRAPHICS4_NVME_DRIVE_HIGH_PERFORMANCE":
            return ec2.InstanceClass.GRAPHICS4_NVME_DRIVE_HIGH_PERFORMANCE
        elif instance_class == "GRAPHICS5":
            return ec2.InstanceClass.GRAPHICS5
        elif instance_class == "GRAPHICS5_GRAVITON2":
            return ec2.InstanceClass.GRAPHICS5_GRAVITON2
        elif instance_class == "H1":
            return ec2.InstanceClass.H1
        elif instance_class == "HIGH_COMPUTE_MEMORY1":
            return ec2.InstanceClass.HIGH_COMPUTE_MEMORY1
        elif instance_class == "HIGH_MEMORY_12TB_1":
            return ec2.InstanceClass.HIGH_MEMORY_12TB_1
        elif instance_class == "HIGH_MEMORY_18TB_1":
            return ec2.InstanceClass.HIGH_MEMORY_18TB_1
        elif instance_class == "HIGH_MEMORY_24TB_1":
            return ec2.InstanceClass.HIGH_MEMORY_24TB_1
        elif instance_class == "HIGH_MEMORY_3TB_1":
            return ec2.InstanceClass.HIGH_MEMORY_3TB_1
        elif instance_class == "HIGH_MEMORY_6TB_1":
            return ec2.InstanceClass.HIGH_MEMORY_6TB_1
        elif instance_class == "HIGH_MEMORY_9TB_1":
            return ec2.InstanceClass.HIGH_MEMORY_9TB_1
        elif instance_class == "HIGH_PERFORMANCE_COMPUTING6_AMD":
            return ec2.InstanceClass.HIGH_PERFORMANCE_COMPUTING6_AMD
        elif instance_class == "HPC6A":
            return ec2.InstanceClass.HPC6A
        elif instance_class == "I3":
            return ec2.InstanceClass.I3
        elif instance_class == "I3EN":
            return ec2.InstanceClass.I3EN
        elif instance_class == "I4I":
            return ec2.InstanceClass.I4I
        elif instance_class == "IM4GN":
            return ec2.InstanceClass.IM4GN
        elif instance_class == "INF1":
            return ec2.InstanceClass.INF1
        elif instance_class == "INFERENCE1":
            return ec2.InstanceClass.INFERENCE1
        elif instance_class == "IO3":
            return ec2.InstanceClass.IO3
        elif instance_class == "IO3_DENSE_NVME_DRIVE":
            return ec2.InstanceClass.IO3_DENSE_NVME_DRIVE
        elif instance_class == "IO4_INTEL":
            return ec2.InstanceClass.IO4_INTEL
        elif instance_class == "IS4GEN":
            return ec2.InstanceClass.IS4GEN
        elif instance_class == "M3":
            return ec2.InstanceClass.M3
        elif instance_class == "M4":
            return ec2.InstanceClass.M4
        elif instance_class == "M5":
            return ec2.InstanceClass.M5
        elif instance_class == "M5A":
            return ec2.InstanceClass.M5A
        elif instance_class == "M5AD":
            return ec2.InstanceClass.M5AD
        elif instance_class == "M5D":
            return ec2.InstanceClass.M5D
        elif instance_class == "M5DN":
            return ec2.InstanceClass.M5DN
        elif instance_class == "M5N":
            return ec2.InstanceClass.M5N
        elif instance_class == "M5ZN":
            return ec2.InstanceClass.M5ZN
        elif instance_class == "M6A":
            return ec2.InstanceClass.M6A
        elif instance_class == "M6G":
            return ec2.InstanceClass.M6G
        elif instance_class == "M6GD":
            return ec2.InstanceClass.M6GD
        elif instance_class == "M6I":
            return ec2.InstanceClass.M6I
        elif instance_class == "M6ID":
            return ec2.InstanceClass.M6ID
        elif instance_class == "MAC1":
            return ec2.InstanceClass.MAC1
        elif instance_class == "MACINTOSH1_INTEL":
            return ec2.InstanceClass.MACINTOSH1_INTEL
        elif instance_class == "MEMORY3":
            return ec2.InstanceClass.MEMORY3
        elif instance_class == "MEMORY4":
            return ec2.InstanceClass.MEMORY4
        elif instance_class == "MEMORY5":
            return ec2.InstanceClass.MEMORY5
        elif instance_class == "MEMORY5_AMD":
            return ec2.InstanceClass.MEMORY5_AMD
        elif instance_class == "MEMORY5_AMD_NVME_DRIVE":
            return ec2.InstanceClass.MEMORY5_AMD_NVME_DRIVE
        elif instance_class == "MEMORY5_EBS_OPTIMIZED":
            return ec2.InstanceClass.MEMORY5_EBS_OPTIMIZED
        elif instance_class == "MEMORY5_HIGH_PERFORMANCE":
            return ec2.InstanceClass.MEMORY5_HIGH_PERFORMANCE
        elif instance_class == "MEMORY5_NVME_DRIVE":
            return ec2.InstanceClass.MEMORY5_NVME_DRIVE
        elif instance_class == "MEMORY5_NVME_DRIVE_HIGH_PERFORMANCE":
            return ec2.InstanceClass.MEMORY5_NVME_DRIVE_HIGH_PERFORMANCE
        elif instance_class == "MEMORY6_AMD":
            return ec2.InstanceClass.MEMORY6_AMD
        elif instance_class == "MEMORY6_GRAVITON":
            return ec2.InstanceClass.MEMORY6_GRAVITON
        elif instance_class == "MEMORY6_GRAVITON2_NVME_DRIVE":
            return ec2.InstanceClass.MEMORY6_GRAVITON2_NVME_DRIVE
        elif instance_class == "MEMORY6_INTEL":
            return ec2.InstanceClass.MEMORY6_INTEL
        elif instance_class == "MEMORY6_INTEL_NVME_DRIVE":
            return ec2.InstanceClass.MEMORY6_INTEL_NVME_DRIVE
        elif instance_class == "MEMORY_INTENSIVE_1":
            return ec2.InstanceClass.MEMORY_INTENSIVE_1
        elif instance_class == "MEMORY_INTENSIVE_1_EXTENDED":
            return ec2.InstanceClass.MEMORY_INTENSIVE_1_EXTENDED
        elif instance_class == "MEMORY_INTENSIVE_2_GRAVITON2":
            return ec2.InstanceClass.MEMORY_INTENSIVE_2_GRAVITON2
        elif instance_class == "MEMORY_INTENSIVE_2_GRAVITON2_NVME_DRIVE":
            return ec2.InstanceClass.MEMORY_INTENSIVE_2_GRAVITON2_NVME_DRIVE
        elif instance_class == "MEMORY_INTENSIVE_2_INTEL":
            return ec2.InstanceClass.MEMORY_INTENSIVE_2_INTEL
        elif instance_class == "MEMORY_INTENSIVE_2_XTZ_INTEL":
            return ec2.InstanceClass.MEMORY_INTENSIVE_2_XTZ_INTEL
        elif instance_class == "MEMORY_INTENSIVE_2_XT_INTEL":
            return ec2.InstanceClass.MEMORY_INTENSIVE_2_XT_INTEL
        elif instance_class == "P2":
            return ec2.InstanceClass.P2
        elif instance_class == "P3":
            return ec2.InstanceClass.P3
        elif instance_class == "P3DN":
            return ec2.InstanceClass.P3DN
        elif instance_class == "P4D":
            return ec2.InstanceClass.P4D
        elif instance_class == "P4DE":
            return ec2.InstanceClass.P4DE
        elif instance_class == "PARALLEL2":
            return ec2.InstanceClass.PARALLEL2
        elif instance_class == "PARALLEL3":
            return ec2.InstanceClass.PARALLEL3
        elif instance_class == "PARALLEL3_NVME_DRIVE_HIGH_PERFORMANCE":
            return ec2.InstanceClass.PARALLEL3_NVME_DRIVE_HIGH_PERFORMANCE
        elif instance_class == "PARALLEL4":
            return ec2.InstanceClass.PARALLEL4
        elif instance_class == "PARALLEL4_NVME_DRIVE_EXTENDED":
            return ec2.InstanceClass.PARALLEL4_NVME_DRIVE_EXTENDED
        elif instance_class == "R3":
            return ec2.InstanceClass.R3
        elif instance_class == "R4":
            return ec2.InstanceClass.R4
        elif instance_class == "R5":
            return ec2.InstanceClass.R5
        elif instance_class == "R5A":
            return ec2.InstanceClass.R5A
        elif instance_class == "R5AD":
            return ec2.InstanceClass.R5AD
        elif instance_class == "R5B":
            return ec2.InstanceClass.R5B
        elif instance_class == "R5D":
            return ec2.InstanceClass.R5D
        elif instance_class == "R5DN":
            return ec2.InstanceClass.R5DN
        elif instance_class == "R5N":
            return ec2.InstanceClass.R5N
        elif instance_class == "R6A":
            return ec2.InstanceClass.R6A
        elif instance_class == "R6G":
            return ec2.InstanceClass.R6G
        elif instance_class == "R6GD":
            return ec2.InstanceClass.R6GD
        elif instance_class == "R6I":
            return ec2.InstanceClass.R6I
        elif instance_class == "R6ID":
            return ec2.InstanceClass.R6ID
        elif instance_class == "STANDARD3":
            return ec2.InstanceClass.STANDARD3
        elif instance_class == "STANDARD4":
            return ec2.InstanceClass.STANDARD4
        elif instance_class == "STANDARD5":
            return ec2.InstanceClass.STANDARD5
        elif instance_class == "STANDARD5_AMD":
            return ec2.InstanceClass.STANDARD5_AMD
        elif instance_class == "STANDARD5_AMD_NVME_DRIVE":
            return ec2.InstanceClass.STANDARD5_AMD_NVME_DRIVE
        elif instance_class == "STANDARD5_HIGH_COMPUTE":
            return ec2.InstanceClass.STANDARD5_HIGH_COMPUTE
        elif instance_class == "STANDARD5_HIGH_PERFORMANCE":
            return ec2.InstanceClass.STANDARD5_HIGH_PERFORMANCE
        elif instance_class == "STANDARD5_NVME_DRIVE":
            return ec2.InstanceClass.STANDARD5_NVME_DRIVE
        elif instance_class == "STANDARD5_NVME_DRIVE_HIGH_PERFORMANCE":
            return ec2.InstanceClass.STANDARD5_NVME_DRIVE_HIGH_PERFORMANCE
        elif instance_class == "STANDARD6_AMD":
            return ec2.InstanceClass.STANDARD6_AMD
        elif instance_class == "STANDARD6_GRAVITON":
            return ec2.InstanceClass.STANDARD6_GRAVITON
        elif instance_class == "STANDARD6_GRAVITON2_NVME_DRIVE":
            return ec2.InstanceClass.STANDARD6_GRAVITON2_NVME_DRIVE
        elif instance_class == "STANDARD6_INTEL":
            return ec2.InstanceClass.STANDARD6_INTEL
        elif instance_class == "STANDARD6_INTEL_NVME_DRIVE":
            return ec2.InstanceClass.STANDARD6_INTEL_NVME_DRIVE
        elif instance_class == "STORAGE2":
            return ec2.InstanceClass.STORAGE2
        elif instance_class == "STORAGE3":
            return ec2.InstanceClass.STORAGE3
        elif instance_class == "STORAGE3_ENHANCED_NETWORK":
            return ec2.InstanceClass.STORAGE3_ENHANCED_NETWORK
        elif instance_class == "STORAGE4_GRAVITON_NETWORK_OPTIMIZED":
            return ec2.InstanceClass.STORAGE4_GRAVITON_NETWORK_OPTIMIZED
        elif instance_class == "STORAGE4_GRAVITON_NETWORK_STORAGE_OPTIMIZED":
            return ec2.InstanceClass.STORAGE4_GRAVITON_NETWORK_STORAGE_OPTIMIZED
        elif instance_class == "STORAGE_COMPUTE_1":
            return ec2.InstanceClass.STORAGE_COMPUTE_1
        elif instance_class == "T2":
            return ec2.InstanceClass.T2
        elif instance_class == "T3":
            return ec2.InstanceClass.T3
        elif instance_class == "T3A":
            return ec2.InstanceClass.T3A
        elif instance_class == "T4G":
            return ec2.InstanceClass.T4G
        elif instance_class == "U_12TB1":
            return ec2.InstanceClass.U_12TB1
        elif instance_class == "U_18TB1":
            return ec2.InstanceClass.U_18TB1
        elif instance_class == "U_24TB1":
            return ec2.InstanceClass.U_24TB1
        elif instance_class == "U_3TB1":
            return ec2.InstanceClass.U_3TB1
        elif instance_class == "U_6TB1":
            return ec2.InstanceClass.U_6TB1
        elif instance_class == "U_9TB1":
            return ec2.InstanceClass.U_9TB1
        elif instance_class == "VIDEO_TRANSCODING1":
            return ec2.InstanceClass.VIDEO_TRANSCODING1
        elif instance_class == "VT1":
            return ec2.InstanceClass.VT1
        elif instance_class == "X1":
            return ec2.InstanceClass.X1
        elif instance_class == "X1E":
            return ec2.InstanceClass.X1E
        elif instance_class == "X2G":
            return ec2.InstanceClass.X2G
        elif instance_class == "X2GD":
            return ec2.InstanceClass.X2GD
        elif instance_class == "X2IDN":
            return ec2.InstanceClass.X2IDN
        elif instance_class == "X2IEDN":
            return ec2.InstanceClass.X2IEDN
        elif instance_class == "X2IEZN":
            return ec2.InstanceClass.X2IEZN
        elif instance_class == "Z1D":
            return ec2.InstanceClass.Z1D
        else:
            logger.info(f"[ERROR]: getEC2ReplicationInstanceClass: {instance_class}")
            return None

    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/InstanceSize.html
    # Full List provisioned on 2022_09_19

    def getEC2ReplicationInstanceSize(instance_size: str) ->  Union[ec2.InstanceSize, None]:
        """Returns the instance size for the EC2 machine.
        https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/InstanceSize.html

        Args:
            instance_size (str): String for the instance_size (i.e. LARGE, MICRO, XLARGE)

        Returns:
            ec2.InstanceSize | None: Literal value of the instance size or None. i.e. ec2.InstanceSize.MEDIUM
        """
        if instance_size == "LARGE":
            return ec2.InstanceSize.LARGE
        elif instance_size == "MEDIUM":
            return ec2.InstanceSize.MEDIUM
        elif instance_size == "METAL":
            return ec2.InstanceSize.METAL
        elif instance_size == "MICRO":
            return ec2.InstanceSize.MICRO
        elif instance_size == "NANO":
            return ec2.InstanceSize.NANO
        elif instance_size == "SMALL":
            return ec2.InstanceSize.SMALL
        elif instance_size == "XLARGE":
            return ec2.InstanceSize.XLARGE
        elif instance_size == "XLARGE10":
            return ec2.InstanceSize.XLARGE10
        elif instance_size == "XLARGE112":
            return ec2.InstanceSize.XLARGE112
        elif instance_size == "XLARGE12":
            return ec2.InstanceSize.XLARGE12
        elif instance_size == "XLARGE16":
            return ec2.InstanceSize.XLARGE16
        elif instance_size == "XLARGE18":
            return ec2.InstanceSize.XLARGE18
        elif instance_size == "XLARGE2":
            return ec2.InstanceSize.XLARGE2
        elif instance_size == "XLARGE24":
            return ec2.InstanceSize.XLARGE24
        elif instance_size == "XLARGE3":
            return ec2.InstanceSize.XLARGE3
        elif instance_size == "XLARGE32":
            return ec2.InstanceSize.XLARGE32
        elif instance_size == "XLARGE4":
            return ec2.InstanceSize.XLARGE4
        elif instance_size == "XLARGE48":
            return ec2.InstanceSize.XLARGE48
        elif instance_size == "XLARGE56":
            return ec2.InstanceSize.XLARGE56
        elif instance_size == "XLARGE6":
            return ec2.InstanceSize.XLARGE6
        elif instance_size == "XLARGE8":
            return ec2.InstanceSize.XLARGE8
        elif instance_size == "XLARGE9":
            return ec2.InstanceSize.XLARGE9
        else:
            logger.info(f"[ERROR]: getEC2ReplicationInstanceSize: {instance_size}")
            return None

    # https://docs.aws.amazon.com/cdk/api/v2/python/aws_cdk.aws_ec2/SubnetType.html
    # Full List provisioned on 2022_09_19
    def getEC2Subnet(subnet_type: str) ->  Union[ec2.SubnetType, None]:
        """Returns subnet enumerated type based on the value provided or None if invalid

        Args:
            subnet_type (str): String of the subnet type (i.e. PUBLIC, PRIVATE_WITH_NAT)

        Returns:
            ec2.SubnetType | None: returns enumerated type if valid string provided or None, i.e. ec2.SubnetType.PUBLIC
        """
        if subnet_type == "PRIVATE_ISOLATED":
            return ec2.SubnetType.PRIVATE_ISOLATED
        elif subnet_type == "PRIVATE_WITH_EGRESS":
            return ec2.SubnetType.PRIVATE_WITH_EGRESS
        elif subnet_type == "PRIVATE_WITH_NAT":
            return ec2.SubnetType.PRIVATE_WITH_NAT
        elif subnet_type == "PUBLIC":
            return ec2.SubnetType.PUBLIC
        else:
            logger.info(f"[ERROR]: getEC2Subnet: {subnet_type}")
            return None
