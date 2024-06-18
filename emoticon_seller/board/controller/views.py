from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from board.entity.models import Board
from board.serializers import BoardSerializer
from board.service.board_service_impl import BoardServiceImpl


class BoardView(viewsets.ViewSet):
    queryset = Board.objects.all()
    boardService = BoardServiceImpl.getInstance()

    def list(self, request):
        boardList = self.boardService.list()
        print('boardList:', boardList)
        serializer = BoardSerializer(boardList, many=True)
        print('serialized boardList:', serializer.data)
        return Response(serializer.data)

    def register(self, request):
        try:
            data = request.data

            boardTitle = data.get('boardTitle')
            boardWriter = data.get('boardWriter')
            boardContent = data.get('boardContent')
            if request.FILES.get('boardImage'):
                boardImage = request.FILES.get('boardImage')
            else: boardImage = None

            if not all([boardTitle, boardWriter, boardContent]):
                return Response({'error': '제목, 작성자, 내용은 필수입니다.'},
                                status=status.HTTP_400_BAD_REQUEST)

            self.boardService.registerBoard(boardTitle, boardWriter, boardContent, boardImage)

            serializer = BoardSerializer(data=request.data)

            return Response(status=status.HTTP_200_OK)

        except Exception as e:
            print('게시글 등록 과정 중 문제 발생:', e)
            return Response({'error': str(e)}, status=status.HTTP_400_BAD_REQUEST)