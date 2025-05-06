#include <iostream>
#include <deque>
#include <string>
#include <algorithm>
using namespace std;

deque<int> dq;
int cntB = 0;
int cntW = 0;

void push_dq(int status, string bw) {
	if (bw == "b") {
		if (status == 0) {
			dq.push_back(0);
			cntB++;
		}
		else if (status == 1) {
			if (!dq.empty() && dq.front() == 1) {
				dq.push_back(0);
				cntB++;
			}
			else {
				return;
			}
		}
		else if (status == 2) {
			dq.push_back(0);
			cntB++;
		}
		else if (status == 3) {
			return;
		}
	}
	else if (bw == "w") {
		dq.push_back(1);
		cntW++;
	}
	return;
}

void rotate(int status) {
	if (status == 0) {
		return;
	}
	else if (status == 1) {
		while (!dq.empty() && dq.front() == 0) {
			dq.pop_front();
			cntB--;
		}
		return;
	}
	else if (status == 2) {
		return;
	}
	else if (status == 3) {
		while (!dq.empty() && dq.back() == 0) {
			dq.pop_back();
			cntB--;
		}
		return;
	}
}

int main() {
    ios::sync_with_stdio(false);
    cin.tie(nullptr);
	int Q; cin >> Q;
	int status = 0;

	for (int idx = 0; idx < Q; idx++) {
		string command, bwrl; cin >> command;
		if (command == "push") {
			string bwrl; cin >> bwrl;
			push_dq(status, bwrl);
		}
		else if (command == "rotate") {
			string bwrl; cin >> bwrl;
			if (bwrl == "r") {
				status = (status + 1) % 4;
			}
			else if (bwrl == "l") {
				status = (status + 3) % 4;
			}
			rotate(status);
		}
		else if (command == "count") {
			string bwrl; cin >> bwrl;
			if (bwrl == "b") {
				cout << cntB << "\n";
			}
			else if (bwrl == "w") {
				cout << cntW << "\n";
			}
		}
		else {
			if (!dq.empty()) {
				if (status == 0 || status == 2) {
					if (!dq.empty()) {
						int x = dq.front();
						dq.pop_front();
						if (x == 0) cntB--; else cntW--;
					}
				}
				else if (status == 1) {
					if (!dq.empty()) {
						int x = dq.front();
						dq.pop_front();
						if (x == 0) cntB--; else cntW--;
					}
					while (!dq.empty() && dq.front() == 0) {
						dq.pop_front();
						cntB--;;
					}
				}
				else if (status == 3) {
					if (!dq.empty()) {
						int x = dq.front();
						dq.pop_front();
						if (x == 0) cntB--; else cntW--;
						}
					}
				}
			}
		}
}
