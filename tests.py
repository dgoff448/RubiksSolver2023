"""
File: tests.py
Author: David Goff
Date: 6/19/24
Description: Unit Testing for the simulated rubik's cube.
"""

import unittest

import createCells
import cube


SOLVED = "1\t2	3	4	5	6	7	8	9	10\t11	12	13	14	15	16	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54"


WHITE_CW = "7	8	1	2	3	4	5	6	9	10	11	37	38	39	15	16	17	18	19	20	21	22	12	13	14	26	27	25	29	30	31	32	33	23	24	36	34	35	28	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54"
WHITE_CCW = "3	4	5	6	7	8	1	2	9	10	11	23	24	25	15	16	17	18	19	20	21	22	34	35	28	26	27	39	29	30	31	32	33	37	38	36	12	13	14	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54"
WHITE_DUB = "5	6	7	8	1	2	3	4	9	10	11	34	35	28	15	16	17	18	19	20	21	22	37	38	39	26	27	14	29	30	31	32	33	12	13	36	23	24	25	40	41	42	43	44	45	46	47	48	49	50	51	52	53	54"
																																																						
BLUE_CW = "19	2	3	4	5	6	25	26	9	16	17	10	11	12	13	14	15	18	46	20	21	22	23	24	52	53	27	28	29	30	31	32	33	34	35	36	1	38	39	40	41	42	7	8	45	37	47	48	49	50	51	43	44	54"
BLUE_CCW = "37	2	3	4	5	6	43	44	9	12	13	14	15	16	17	10	11	18	1	20	21	22	23	24	7	8	27	28	29	30	31	32	33	34	35	36	46	38	39	40	41	42	52	53	45	19	47	48	49	50	51	25	26	54"
BLUE_DUB = "46	2	3	4	5	6	52	53	9	14	15	16	17	10	11	12	13	18	37	20	21	22	23	24	43	44	27	28	29	30	31	32	33	34	35	36	19	38	39	40	41	42	25	26	45	1	47	48	49	50	51	7	8	54"
																																																						
RED_CW = "28	29	30	4	5	6	7	8	9	1	2	3	13	14	15	16	17	18	25	26	19	20	21	22	23	24	27	50	51	52	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	10	11	12	53	54"
RED_CCW = "10	11	12	4	5	6	7	8	9	50	51	52	13	14	15	16	17	18	21	22	23	24	25	26	19	20	27	1	2	3	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	28	29	30	53	54"
RED_DUB = "50	51	52	4	5	6	7	8	9	28	29	30	13	14	15	16	17	18	23	24	25	26	19	20	21	22	27	10	11	12	31	32	33	34	35	36	37	38	39	40	41	42	43	44	45	46	47	48	49	1	2	3	53	54"
																																																						
GREEN_CW = "1	2	39	40	41	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	3	4	5	24	25	26	27	34	35	28	29	30	31	32	33	36	37	38	48	49	50	42	43	44	45	46	47	21	22	23	51	52	53	54"
GREEN_CCW = "1	2	21	22	23	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	48	49	50	24	25	26	27	30	31	32	33	34	35	28	29	36	37	38	3	4	5	42	43	44	45	46	47	39	40	41	51	52	53	54"
GREEN_DUB = "1	2	48	49	50	6	7	8	9	10	11	12	13	14	15	16	17	18	19	20	39	40	41	24	25	26	27	32	33	34	35	28	29	30	31	36	37	38	21	22	23	42	43	44	45	46	47	3	4	5	51	52	53	54"
																																																						
ORANGE_CW = "1	2	3	4	14	15	16	8	9	10	11	12	13	46	47	48	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	5	6	7	35	36	43	44	37	38	39	40	41	42	45	32	33	34	49	50	51	52	53	54"
ORANGE_CCW = "1	2	3	4	32	33	34	8	9	10	11	12	13	5	6	7	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	46	47	48	35	36	39	40	41	42	43	44	37	38	45	14	15	16	49	50	51	52	53	54"
ORANGE_DUB = "1	2	3	4	46	47	48	8	9	10	11	12	13	32	33	34	17	18	19	20	21	22	23	24	25	26	27	28	29	30	31	14	15	16	35	36	41	42	43	44	37	38	39	40	45	5	6	7	49	50	51	52	53	54"
																																																						
YELLOW_CW = "1	2	3	4	5	6	7	8	9	21	11	12	13	14	15	19	20	18	30	31	32	22	23	24	25	26	27	28	29	41	42	43	33	34	35	36	37	38	39	40	16	17	10	44	45	52	53	46	47	48	49	50	51	54"
YELLOW_CCW = "1	2	3	4	5	6	7	8	9	43	11	12	13	14	15	41	42	18	16	17	10	22	23	24	25	26	27	28	29	19	20	21	33	34	35	36	37	38	39	40	30	31	32	44	45	48	49	50	51	52	53	46	47	54"
YELLOW_DUB = "1\t2	3	4	5	6	7	8	9	32	11	12	13	14	15	30	31	18	41	42	43	22	23	24	25	26	27	28	29	16	17	10	33	34	35	36	37	38	39	40	19	20	21	44	45	50	51	52	53	46	47	48	49	54"

class TestCube(unittest.TestCase):
    def test_White_CW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.white_CW()
        self.assertEqual(str(cube).replace(' ', '\t'), WHITE_CW)

    def test_White_CCW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.white_CCW()
        self.assertEqual(str(cube).replace(' ', '\t'), WHITE_CCW)

    def test_White_Dub(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.white_Dub()
        self.assertEqual(str(cube).replace(' ', '\t'), WHITE_DUB)

    def test_Blue_CW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.blue_CW()
        self.assertEqual(str(cube).replace(' ', '\t'), BLUE_CW)

    def test_Blue_CCW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.blue_CCW()
        self.assertEqual(str(cube).replace(' ', '\t'), BLUE_CCW)

    def test_Blue_Dub(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.blue_Dub()
        self.assertEqual(str(cube).replace(' ', '\t'), BLUE_DUB)

    def test_Red_CW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.red_CW()
        self.assertEqual(str(cube).replace(' ', '\t'), RED_CW)

    def test_Red_CCW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.red_CCW()
        self.assertEqual(str(cube).replace(' ', '\t'), RED_CCW)

    def test_Red_Dub(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.red_Dub()
        self.assertEqual(str(cube).replace(' ', '\t'), RED_DUB)

    def test_Green_CW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.green_CW()
        self.assertEqual(str(cube).replace(' ', '\t'), GREEN_CW)

    def test_Green_CCW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.green_CCW()
        self.assertEqual(str(cube).replace(' ', '\t'), GREEN_CCW)

    def test_Green_Dub(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.green_Dub()
        self.assertEqual(str(cube).replace(' ', '\t'), GREEN_DUB)

    def test_Orange_CW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.orange_CW()
        self.assertEqual(str(cube).replace(' ', '\t'), ORANGE_CW)

    def test_Orange_CCW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.orange_CCW()
        self.assertEqual(str(cube).replace(' ', '\t'), ORANGE_CCW)

    def test_Orange_Dub(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.orange_Dub()
        self.assertEqual(str(cube).replace(' ', '\t'), ORANGE_DUB)

    def test_Yellow_CW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.yellow_CW()
        self.assertEqual(str(cube).replace(' ', '\t'), YELLOW_CW)

    def test_Yellow_CCW(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.yellow_CCW()
        self.assertEqual(str(cube).replace(' ', '\t'), YELLOW_CCW)

    def test_Yellow_Dub(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.yellow_Dub()
        self.assertEqual(str(cube).replace(' ', '\t'), YELLOW_DUB)

    def test_Multiple_Moves(self):
        cube = cube.Cube(createCells.createCells('testInput/solvedCube.txt'))
        cube.white_CW()
        cube.blue_Dub()
        cube.yellow_Dub()
        cube.yellow_Dub()
        cube.blue_Dub()
        cube.white_CCW()
        self.assertEqual(str(cube).replace(' ', '\t'), SOLVED)

if __name__ == '__main__':
    unittest.main()

