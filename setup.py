from setuptools import setup, find_packages

setup(
    name='infinite_maze_game',
    version='0.1.0',
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'maze-game=main:play_game',
        ],
    },
    author='lihuiruo110',
    description='A terminal-based infinite stage random maze game.',
    classifiers=[
        'Programming Language :: Python :: 3',
        'Topic :: Games/Entertainment :: Puzzle Games',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
