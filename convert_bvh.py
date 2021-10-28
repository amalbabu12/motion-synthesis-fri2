import sys

def generate_skeleton(joints):
    pass

def update_frames(joints, joints, frames):
    # first get indices of joints
    joint_indices = []


if __name__ == '__main__':
    # print(sys.argv[1])
    # will add root automatically
    JOINT_LIST = [
        ['LHipJoint', 'LeftUpLeg', 'LeftLeg'],
        ['RHipJoint', 'RightUpLeg', 'RightLeg'],
        ['LowerBack', 'Spine', 'Spine1']
    ]
    with open(sys.argv[1]) as f:
        lines = [line.rstrip() for line in f.readlines()]

        # Generate hierarchy
        h_lines = lines[1:lines.index('MOTION')]
        updated_hierarchy = generate_skeleton(JOINT_LIST, h_lines)

        # Delete respective joint values from frames
        m_lines = lines[lines.index('MOTION') + 1:]
        updated_frames = update_frames(JOINT_LIST, h_lines, m_lines)