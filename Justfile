run-backend:
	cd backend && just install && just run

run-frontend:
	cd frontend && just install && just run

clean:
	cd backend && just clean
	cd frontend && just clean